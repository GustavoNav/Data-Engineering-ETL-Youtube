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
            
            channel_about = {}
            channel_metrics = {}

            for channel_information in data:

                channel_about ={
                    'channel': channel_information['channel'],
                    'about': channel_information['about'],
                    'creation_date': channel_information['creation_date'],
                    'channel_location': channel_information['channel_location'],
                    'extraction_date': channel_information['extraction_date']
                }

                channel_about ={
                    'channel': channel_information['channel'],
                    'subscriptions': channel_information['subscriptions'],
                    'total_videos': channel_information['total_videos'],
                    'total_views': channel_information['total_views'],
                    'extraction_date': channel_information['extraction_date']
                }

                try:
                    self.__repository.insert_channel_about(channel_about)
                except Exception:
                    pass
                
                self.__repository.insert_channel_metrics(channel_metrics)
        
        except Exception as exception:
            raise LoadError(str(exception)) from exception
