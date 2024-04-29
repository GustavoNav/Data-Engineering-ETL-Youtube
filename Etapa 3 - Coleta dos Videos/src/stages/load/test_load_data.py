from .load_data import LoadData
from src.infra.database_repository import DatabaseRepository
from src.infra.database_connector import DatabaseConnector


def test_load_data():
    DatabaseConnector.connect()
 
    repository = DatabaseRepository()
    load_data = LoadData(repository)

    load_data.load()