import time
import json
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.infra.database_repository import DatabaseRepository
from src.infra.database_connector import DatabaseConnector
from src.drivers.interfaces.html_collector import HtmlCollectorInterface


class HttpRequester():
    def __init__(self, html_collector: HtmlCollectorInterface) -> None:
        self.html_collector = html_collector

    def request_from_pages(self, urls: list) -> None:
        browser = webdriver.Firefox()
        
        file = "src\\data\\extract_data.json"
        with open(file, "w") as file_json:
            file_json.write('')

        with open(file, "a", encoding='utf-8') as file_json:

            data = []
            for dict in urls:
                video_id = dict['video_id']
                channel = dict['channel']
                url = dict['video_link']

                try:
                    browser.get(url)
                except:
                    continue

                time.sleep(5)
                browser.execute_script("window.scrollTo(0, 500);")
                
                time.sleep(5)

                html = browser.page_source
                informations = self.html_collector.collect_essential_information(html)

                extraction_date = date.today()
                extraction_date_str = extraction_date.strftime('%Y-%m-%d')

                essential_informations = {'video_id': video_id,'channel': channel,'extraction_date': extraction_date_str, 'essential_information': informations}
                data.append(essential_informations)

            json.dump(data, file_json, ensure_ascii=False, indent=4)

        browser.quit()
        

    def set_urls(self) -> list:
        database_connector = DatabaseConnector()
        database_connector.connect()

        database_repository = DatabaseRepository()
        urls = database_repository.select_channel()

        return urls
