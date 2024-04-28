'''Connector da Database'''
import mysql.connector as mysql

class DatabaseConnector:
    '''Classe responsável por fazer a conexão com o Banco de Dados Local'''
    connection = None
    @classmethod
    def connect(cls) -> None:
        db_connection = mysql.connect(
            host='localhost',
            port=3306,
            database='pipeline_db',
            user='root',
            passwd='adm321'
        )
        cls.connection = db_connection