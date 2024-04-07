'''Inserção de dados'''
from typing import Dict
from .database_connector import DatabaseConnector

class DatabaseRepository():
    '''Classe responsável por fazer o INSERT dos dados no banco de dados'''
    @classmethod
    def insert_channel(cls, data: Dict) -> None:
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
    def select_channel(cls) -> None:
        query='''
                SELECT DISTINCT channel, link
                FROM videos
            '''
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query)

        result = cursor.fetchall()
        
        information = []
        for tupla in result:
            channel = str(tupla[0])
            link = str(tupla[1])
            information.append({'channel': channel, 'link': link})

        return information