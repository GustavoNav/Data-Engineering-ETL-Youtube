# ETL - Youtube

## Descrição
Esse é um projeto pessoal para por em pratica conceitos de Data Engineering, Data analytics e Data Science.
O Projeto será divido em Etapas, que serão desenvolvidas e publicadas ao longo do primeiro semestre de 2024.

A arquitetura do projeto e ideia foram inspirados no conjunto de aulas de ETL Pipeline do [Programador Lhama](https://www.youtube.com/watch?v=D5mwXMMA0e0&list=PLAgbpJQADBGLuI1oR39tVfELOEZJSSbxQ).

## Requisitos
Projeto executado no Python 3.12, não testado em outras versões.

Primeiro clone o repositório, crie o ambiente virtual, ative o ambiente e instale o requirements.
### Windows

```
git clone https://github.com/GustavoNav/Data-Engineering-ETL-Youtube
python3 -m venv nome_do_ambiente
nome_do_ambiente\Scripts\activate
pip install -r requirements.txt
```
### Mac/Linux

```
git clone https://github.com/GustavoNav/ETL-Youtube
python3 -m venv nome_do_ambiente
source nome_do_ambiente/bin/activate
pip install -r ETL-Youtube/requirements.txt
```

### Banco de Dados
O banco de dados utilizados é Mysql, a conexão foi criada utilizando o DBeaver, detalhes da conexão no arquivo *database_connector*, código para criação do database e das tabelas diponível no arquivo *db.sql*
```
CREATE DATABASE IF NOT EXISTS pipeline_db;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`videos`(
id BIGINT NOT NULL AUTO_INCREMENT,
channel VARCHAR(255),
title VARCHAR(255),
link VARCHAR(255),
views INTEGER,
video_time VARCHAR(255),
time_online VARCHAR(255),
extraction_date DATETIME NOT NULL,
primary key(id)
) ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`canais_sobre`(
id BIGINT NOT NULL AUTO_INCREMENT,
channel VARCHAR(255) UNIQUE,
about TEXT,
creation_date DATETIME,
channel_location VARCHAR(255),
extraction_date DATETIME NOT NULL,
primary key(id)
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS `pipeline_db`.`canais_metricas`(
id BIGINT NOT NULL AUTO_INCREMENT,
channel VARCHAR(255),
subscriptions VARCHAR(255),
total_videos INTEGER,
total_views BIGINT,
extraction_date DATETIME NOT NULL,
primary key(id)
)ENGINE=INNODB;
```

### Navegador
É utilizado o selenium para realizar a coleta dos dados, para utilizar o selenium é necessário a instalação do navegador [FireFox](https://www.mozilla.org/en-US/firefox/new/)

É necessária a instalação drive do FireFox: [geckodriver](https://github.com/mozilla/geckodriver/releases)

Uma vez instalado é necessário configurar a váriavel de ambiente, adicione o diretório onde o driver está localizado à variável de ambiente PATH do seu sistema operacional.

### Etapa 1 - Web Scraping
Essa pipeline realiza a extração de dados de videos do '*Em Alta*' do Youtube, realiza transformação no conjunto de dados e então carrega em um banco de Dados.

Diagrama de Classes:
![alt text](<Etapa 1 - Web Scraping/Diagrama_de_classes_Etapa1.png>)

* Drivers

Local onde os dados do youtube são requisitados, a classe *HttpRequester* faz a requisição, utilizando da biblioteca selenium para abrir o site e então aguardar o carregamento, para recolher todo o html. Em seguida o *HtmlCollector* coleta a informação de interesse do Html, que se refere aos videos.

* Extração

O estágio de extração utiliza da classe *ExtractHTML* para fazer a chamada das classes do Drive, e então devolve as dados em um contrato de extração (namedtuple).

* Transformação

O estágio mais complexo, a classe 'TransformHtml' transforma o HTML, coletando as informações relevantes com a biblioteca re: **Titulo**, **Canal**, **Visualizações**, **Tempo de Video**, **Tempo do lançamento**, **Link**, **Data de Extração**. Então é retornado um contrato de transformação.  

* Carga

O estágio reponsável pela injeção de dados, a classe LoadData utiliza o repositório e connection para inserir o dados ao banco de dados.

* Infra

A classe *DatabaseConnector* é reponsável por fazer a conexão com o banco de dados, e então a *DatabaseRepository* realiza a injeção de dados no banco de dados.

### Execução
Basta acessar o diretório *Etapa 1 - Web Scraping* basta executar o arquivo *run.py*

É esperado que uma aba no firefox seja aberta por 20 segundos para coleta de dados e então fechadado, por fim os dados serão carregados.

```
cd Etapa 1 - Web Scraping
python3 run.py
```

### Etapa 2 - Expandindo o Banco de Dados
Essa etapa tem como objetivo criar um pipeline que coleta informações do banco de dados locais e as utilizada para fazer web scraping, realizar transformações e carregar em uma nova tabela.

Diagrama de Classes:
![alt text](<Etapa 2 - Expandindo o Banco de Dados/Diagrama_de_classe_Etapa2.png>)

* Drivers

Diferente da primeira pipeline, os dados já sofrem uma filtragem em tempo de coleta. Com o HttpRepository é realizada uma consulta ao banco de dados, afim de obter o nome dos canais e os links para retornar em forma de lista, então o *HttpRequester* acessa a url de cada canal com o selenium. Ao selecionar o HTML da pagina, o *HtmlCollector* executa uma filtragem, selecionando apenas a parte de interesse. Por fim as informações em HTML são salvas em um arquivo JSON.

* Extração

O estágio de extração utiliza da classe *ExtractHTML* para fazer a chamada das classes do Drive, e então salvar em uma arquivo JSON.

* Transformação

Esse estágio se concentra em localizar e guardar as informações de interesse dos dados, é utilizado REGEX para realizar as buscas. Então as informações são organizadas e salvas em um arquivo JSON. 

* Carga

O estágio reponsável pela injeção de dados, a classe LoadData utiliza o repositório e connection para inserir o dados ao banco de dados, em duas tabelas: *canal_sobre* e *canal_metricas*

* Infra

A classe *DatabaseConnector* é reponsável por fazer a conexão com o banco de dados, e então a *DatabaseRepository* pode fazer comandos SQL, como SELECT e INSERT.



## Links Úteis 
[Python](https://www.python.org/)

[Selenium](https://www.selenium.dev/)

[BeatifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)

[Youtube Trending](https://www.youtube.com/feed/trending)
