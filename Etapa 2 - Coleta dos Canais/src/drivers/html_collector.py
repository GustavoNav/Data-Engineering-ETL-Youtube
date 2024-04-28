from bs4 import BeautifulSoup
from src.drivers.interfaces.html_collector import HtmlCollectorInterface

class HtmlCollector(HtmlCollectorInterface):
    @classmethod
    def collect_essential_information(cls, html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        about = soup.find('ytd-popup-container', class_='style-scope ytd-app')
        about_informations = str(about.find('ytd-engagement-panel-section-list-renderer', class_='style-scope ytd-popup-container'))


        return about_informations
