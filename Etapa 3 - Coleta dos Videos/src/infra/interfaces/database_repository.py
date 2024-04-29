from abc import ABC
from abc import abstractmethod
from typing import Dict

class DatabaseRepositoryInterface(ABC):
    @abstractmethod
    def select_channel(self) -> None:
        pass
    
    @abstractmethod
    def insert_video_details(self, data: Dict) -> None:
        pass