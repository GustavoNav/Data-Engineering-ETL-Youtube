import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .html_collector import HtmlCollector
from src.infra.database_repository import DatabaseRepository
from src.infra.database_connector import DatabaseConnector

class HttpRequester():
    def __init__(self) -> None:
        self.html_collector = HtmlCollector()

    def request_from_pages(self, urls: list) -> None:
        browser = webdriver.Firefox()
        
        file = "src/drivers/essential_information.json"
        with open(file, "w") as file_json:
            file_json.write('[\n')

        with open(file, "a") as file_json:
            count = 1
            for dict in urls:
                channel = dict['channel']
                url = dict['link']
            
                browser.get(url)
                time.sleep(3)

                self.__click_button(browser)

                time.sleep(3)
                html = browser.page_source

                about_informations = self.html_collector.collect_essential_information(html)
                essential_informations = {'channel': channel, 'essential_information': about_informations}

                json.dump(essential_informations, file_json)
                if count < len(urls):file_json.write(',\n')
                count += 1

            file_json.write('\n]')
        browser.quit()
        

    def set_urls(self) -> list:
        database_connector = DatabaseConnector()
        database_connector.connect()

        database_repository = DatabaseRepository()
        urls = database_repository.select_channel()

        return urls
    
    def __click_button(self, browser) -> None:
                botao = browser.find_element(By.CLASS_NAME, "style-scope ytd-channel-tagline-renderer")
                botao.click()