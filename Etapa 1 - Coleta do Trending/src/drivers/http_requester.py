'''Requisitar html da pagina.'''
import time
from selenium import webdriver
from src.drivers.interfaces.http_requester import HttpRequesterInterface

class HttpRequester(HttpRequesterInterface):
    '''Classe reponsável pela requisição e devolução do html apartir de uma URL.'''
    def __init__(self) -> None:
        self.__url = "https://www.youtube.com/feed/trending"

    def request_from_page(self):
        '''Requisita o html da pagina e retorna dentro de um dicionario.'''
        browser = webdriver.Firefox()
        browser.get(self.__url)

        time.sleep(20)
        html = browser.page_source
        browser.quit()

        return {
            "html": html
        }
