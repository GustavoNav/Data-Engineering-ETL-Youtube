from selenium import webdriver
from src.infra.database_connector import DatabaseConnector
from src.infra.database_repository import DatabaseRepository

class HttpRequester:

    def __init__(self):
        self.__urls = set_urls()


    def request_from_page():
        browser = webdriver.Firefox()

        html_list = []
        for tupla in self.urls:
            
            browser.get(tupla[1])
        
            html = browser.page_source
            html_list.append({'channel':tupla[0], 'html': html})

        browser.quit()

        return html_list

    def __set_urls():
        DatabaseRepository.connect()
        result = DatabaseRepository().select_channel()

        return result