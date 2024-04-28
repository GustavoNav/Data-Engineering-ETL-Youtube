'''Coletar informções relevantes do HTML'''
from bs4 import BeautifulSoup
from src.drivers.interfaces.html_collector import HtmlCollectorInterface

class HtmlCollector(HtmlCollectorInterface):
    '''Classe responsável por coletar informações relevantes do HTML.''' 
    @classmethod
    def collect_essential_information(cls, html: str):
        '''Função única e principal da Classe'''
        soup = BeautifulSoup(html, 'html.parser')
        divs_a = soup.find_all('div', {'id': 'title-wrapper'})
        divs_metadata = soup.find_all('div', class_='text-wrapper style-scope ytd-video-renderer')
        time_span = soup.find_all('span', class_='style-scope ytd-thumbnail-overlay-time-status-renderer')


        videos_text = []
        for div in divs_a:
            a_element = div.find('a')
            videos_text.append(str(a_element))
        
        videos_meta = []
        for div in divs_metadata:
            div_element = div.find('div', class_='style-scope ytd-video-meta-block')
            videos_meta.append(str(div_element))
        
        videos_time = []
        for span in time_span:
            time = span.get_text(strip=True)
            videos_time.append(str(time))

        essential_information = []
        for element in range(len(videos_text)):
            essential_information.append(videos_text[element] + videos_meta[element] + 'time="' + videos_time[element] + '"')

        return essential_information
