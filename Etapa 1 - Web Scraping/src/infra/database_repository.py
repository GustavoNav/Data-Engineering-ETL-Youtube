'''Inserção de dados'''
from typing import Dict
from .database_connector import DatabaseConnector
from .interfaces.database_repository_interface import DatabaseRepositoryInterface

class DatabaseRepository(DatabaseRepositoryInterface):
    '''Classe responsável por fazer o INSERT dos dados no banco de dados'''
    @classmethod
    def insert_video(cls, data: Dict):
        query='''
            INSERT INTO videos
                (title, channel, link, views, video_time, time_online, extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s, %s)
            '''
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnector.connection.commit()