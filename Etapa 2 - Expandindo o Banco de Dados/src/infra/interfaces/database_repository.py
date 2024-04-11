from abc import ABC, abstractmethod
from typing import Dict

class DatabaseRepositoryInterface(ABC):
    @abstractmethod
    def insert_channel_about(self, data: Dict) -> None:
        pass

    @abstractmethod
    def insert_channel_metrics(self, data: Dict) -> None:
        pass

    @abstractmethod
    def select_channel(self) -> None:
        pass