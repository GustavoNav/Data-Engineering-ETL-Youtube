import json
from src.infra.interfaces.database_repository import DatabaseRepositoryInterface
from src.errors.load_error import LoadError

class LoadData:
    def __init__(self, repository: DatabaseRepositoryInterface) -> None:
        self.__repository = repository

    def load(self) -> None:
        try:
            with open('Etapa 3 - Coleta dos Videos\\src\\data\\transformed_data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            for information in data:
                self.__repository.insert_video_details(information)

        except Exception as exception:
            raise LoadError(str(exception)) from exception
