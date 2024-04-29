from datetime import date
from typing import Dict
from src.infra.database_connector import DatabaseConnector

class DatabaseRepository:
    @classmethod
    def select_channel(cls) -> None:
        query=f'''
                SELECT id, channel, video_link
                FROM videos
                WHERE extraction_date = '{date.today()}'
            '''
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query)

        result = cursor.fetchall()
        
        information = []
        for tupla in result:
            video_id = str(tupla[0])
            channel = str(tupla[1])
            link = str(tupla[2])
            information.append({'video_id': video_id,'channel': channel, 'video_link': link})

        return information
    
    @classmethod
    def insert_video_details(cls, data: Dict) -> None:
        query='''
            INSERT INTO videos_detalhes
                (video_id, channel, likes, total_comments, tags, extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s)
            '''
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnector.connection.commit()