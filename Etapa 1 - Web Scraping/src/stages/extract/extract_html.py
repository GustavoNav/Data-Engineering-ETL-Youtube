'''Extrair dados'''
from datetime import date
from src.contracts.extract_contract import ExtractContract
from src.drivers.interfaces.http_requester import HttpRequesterInterface
from src.drivers.interfaces.html_collector import HtmlCollectorInterface
from src.errors.extract_error import ExtractionError

class ExtractHtml:
    '''Classe reponsável pela extração de dados'''
    def __init__(self, http_requester: HttpRequesterInterface, html_collector: HtmlCollectorInterface) -> None:
        self.__http_requester = http_requester
        self.__html_collector = html_collector

    def extract(self,):
        '''Extrai os dados e então retorna um ExtractContract'''
        try:
            html_information = self.__http_requester.request_from_page()
            essential_information = self.__html_collector.collect_essential_information(html_information['html'])

            return ExtractContract(
                raw_information=essential_information,
                extraction_date=date.today()
            )
        except Exception as exception:
            raise ExtractionError(str(exception)) from exception
