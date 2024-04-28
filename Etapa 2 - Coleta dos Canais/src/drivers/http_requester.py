import time
import json
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.drivers.interfaces.http_requester import HttpRequesterInterface
from src.drivers.interfaces.html_collector import HtmlCollectorInterface
from src.infra.database_repository import DatabaseRepository
from src.infra.database_connector import DatabaseConnector


class HttpRequester(HttpRequesterInterface):
    def __init__(self, html_collector: HtmlCollectorInterface) -> None:
        self.html_collector = html_collector

    def request_from_pages(self, urls: list) -> None:
        browser = webdriver.Firefox()
        
        file = "src\data\extract_data.json"
        with open(file, "w") as file_json:
            file_json.write('')

        with open(file, "a", encoding='utf-8') as file_json:
            data = []
            for dict in urls:
                channel = dict['channel']
                url = dict['link']

                try:
                    browser.get(url)
                except:
                    continue

                time.sleep(3)

                try:
                    botao = browser.find_element(By.CLASS_NAME, "style-scope ytd-channel-tagline-renderer")
                    botao.click()
                except:
                    continue

                time.sleep(3)
                html = browser.page_source

                about_informations = self.html_collector.collect_essential_information(html)
                extraction_date = date.today()
                extraction_date_str = extraction_date.strftime('%Y-%m-%d')

                essential_informations = {'channel': channel, 'essential_information': about_informations, 'extraction_date': extraction_date_str}
                data.append(essential_informations)

            json.dump(data, file_json, ensure_ascii=False, indent=4)
            
        browser.quit()
        

    def set_urls(self) -> list:
        database_connector = DatabaseConnector()
        database_connector.connect()

        database_repository = DatabaseRepository()
        urls = database_repository.select_channel()

        return urls
