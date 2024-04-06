from .database_connector import DatabaseConnector
from .database_repository import DatabaseRepository

def test_select_channel():
    DatabaseConnector.connect()
    result = DatabaseRepository().select_channel()
    print(len(result))