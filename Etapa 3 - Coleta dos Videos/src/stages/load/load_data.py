import json
from src.utils.paths import encontrar_caminho
from src.infra.interfaces.database_repository import DatabaseRepositoryInterface
from src.errors.load_error import LoadError

class LoadData:
    def __init__(self, repository: DatabaseRepositoryInterface) -> None:
        self.__repository = repository

    def load(self) -> None:
        try:
            tranform_file = encontrar_caminho('export\\transform\\transformed_data.json')
            with open(tranform_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            for information in data:
                self.__repository.insert_video_details(information)

        except Exception as exception:
            raise LoadError(str(exception)) from exception
