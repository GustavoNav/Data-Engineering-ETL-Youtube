from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector
from src.infra.database_connector import DatabaseConnector
from src.infra.database_repository import DatabaseRepository
from src.stages.extract.extract_html import ExtractHtml
from src.stages.transform.transform_Information import TransformInformation
from src.stages.load.load_data import LoadData

class MainPipeline:
    '''Classe responsável pela execução de todos os estágios da Pipeline'''
    def __init__(self) -> None:
        self.__html_collecor =  HtmlCollector()
        self.__extract_html = ExtractHtml(HttpRequester(self.__html_collecor))
        self.__transform_information = TransformInformation()
        self.__load_data = LoadData(DatabaseRepository())
    
    def run_pipeline(self):
        DatabaseConnector.connect()

        self.__extract_html.extract()
        self.__transform_information.tranform()
        self.__load_data.load()
