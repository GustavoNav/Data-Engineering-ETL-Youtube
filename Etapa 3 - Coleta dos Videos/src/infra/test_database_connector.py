from src.infra.database_connector import DatabaseConnector

def test_connect():
    database_connector = DatabaseConnector()
    database_connector.connect()
    print(database_connector.connection)