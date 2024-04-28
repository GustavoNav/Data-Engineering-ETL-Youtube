from .load_data import  LoadData
from src.infra.database_repository import DatabaseRepository
from src.contracts.mocks.transform_contract_mock import transform_contract_mock

class RepositorySpy:
    def __init__(self) -> None:
        self.insert_artist_attributes = []

    def insert_video(self, data):
        self.insert_artist_attributes.append(data)

def test_load():
    repo = RepositorySpy()
    load_data = LoadData(repo)

    load_data.load(transform_contract_mock)