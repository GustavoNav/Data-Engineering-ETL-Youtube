import os

def encontrar_caminho(diretorio):
    # Obtém o diretório do script atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Navega para cima dois diretórios (..) para chegar ao diretório raiz do projeto
    diretorio_raiz = os.path.join(diretorio_atual, "..", "..")
    
    # Monta o caminho completo para o diretório especificado
    caminho_completo = os.path.join(diretorio_raiz, diretorio)
    
    return caminho_completo