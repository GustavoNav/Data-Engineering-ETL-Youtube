'''Inserção de dados'''
from typing import Dict
from .database_connector import DatabaseConnector

class DatabaseRepository():
    '''Classe responsável por fazer o INSERT dos dados no banco de dados'''
    @classmethod
    def insert_channel(cls, data: Dict):
        query='''
            INSERT INTO canais
                (channel, about, subscriptions, total_videos, total_views, creation_date, channel_location)
            VALUES
                (%s, %s, %s, %s, %s, %s, %s)
            '''
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnector.connection.commit()
    
    @classmethod
    def select_channel(cls):
        query='''
                SELECT DISTINCT channel, link
                FROM videos
            '''
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query)

        result = cursor.fetchall()
        return result