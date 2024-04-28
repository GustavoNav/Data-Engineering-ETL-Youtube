'''Carregar dados'''
from src.infra.interfaces.database_repository_interface import DatabaseRepositoryInterface
from src.contracts.transform_contract import TransformContract
from src.errors.load_error import LoadError

class LoadData:
    '''Classe responsável pela carga dos dados ao Banco de Dados'''
    def __init__(self, repository: DatabaseRepositoryInterface) -> None:
        self.__repository = repository

    def load(self, transformed_data_contract: TransformContract):
        try:
            load_content = transformed_data_contract.load_content
            for data in load_content:
                self.__repository.insert_video(data)

        except Exception as exception:
            raise LoadError(str(exception)) from exception
