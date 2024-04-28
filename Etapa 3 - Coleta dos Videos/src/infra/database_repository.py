from datetime import date
from src.infra.database_connector import DatabaseConnector

class DatabaseRepository:
    @classmethod
    def select_channel(cls) -> None:
        query=f'''
                SELECT channel, video_link
                FROM videos
                WHERE extraction_date = '{date.today()}'
            '''
        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query)

        result = cursor.fetchall()
        
        information = []
        for tupla in result:
            channel = str(tupla[0])
            link = str(tupla[1])
            information.append({'channel': channel, 'video_link': link})

        return information