'''Coletar informções relevantes do HTML'''
from bs4 import BeautifulSoup
from src.drivers.interfaces.html_collector import HtmlCollectorInterface

class HtmlCollector(HtmlCollectorInterface):
    '''Classe responsável por coletar informações relevantes do HTML.''' 
    @classmethod
    def collect_essential_information(cls, html: str):
        '''Função única e principal da Classe'''
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup.find_all('div', {'id': 'title-wrapper'})
        time_span = soup.find_all('span', class_='style-scope ytd-thumbnail-overlay-time-status-renderer')

        videos_text = []
        for div in divs:
            a_element = div.find('a')
            videos_text.append(str(a_element))
        
        videos_time = []
        for span in time_span:
            time = span.get_text(strip=True)
            videos_time.append(str(time))

        essential_information = []
        for element in range(len(videos_text)):
            essential_information.append(videos_text[element] + 'time="' + videos_time[element] + '"')

        return essential_information
