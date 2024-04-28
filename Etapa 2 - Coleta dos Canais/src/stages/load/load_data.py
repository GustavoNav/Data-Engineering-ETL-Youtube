import json
from src.infra.interfaces.database_repository import DatabaseRepositoryInterface
from src.errors.load_error import LoadError

class LoadData:
    def __init__(self, repository: DatabaseRepositoryInterface) -> None:
        self.__repository = repository

    def load(self) -> None:
        try:
            with open('src\\data\\transformed_data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            channel_about = {}
            channel_metrics = {}
            for channel_information in data:

                channel_about['channel'] = channel_information['channel']
                channel_about['about'] = channel_information['about']
                channel_about['creation_date'] = channel_information['creation_date']
                channel_about['channel_location'] = channel_information['channel_location']
                channel_about['extraction_date'] = channel_information['extraction_date']

                channel_metrics['channel'] = channel_information['channel']
                channel_metrics['subscriptions'] = channel_information['subscriptions']
                channel_metrics['total_videos']= channel_information['total_videos']
                channel_metrics['total_views']= channel_information['total_views']
                channel_metrics['extraction_date']= channel_information['extraction_date']

                try:
                    self.__repository.insert_channel_about(channel_about)
                except Exception:
                    pass
                
                self.__repository.insert_channel_metrics(channel_metrics)
        
        except Exception as exception:
            raise LoadError(str(exception)) from exception
