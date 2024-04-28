from datetime import date
from src.infra.database_connector import DatabaseConnector
from src.infra.database_repository import DatabaseRepository

def test_select_channel():
    DatabaseConnector.connect()
    result = DatabaseRepository().select_channel()
    print(date.today())
    print(result)