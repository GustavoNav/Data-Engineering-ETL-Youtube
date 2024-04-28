from typing import Dict
from abc import ABC, abstractmethod

class DatabaseRepositoryInterface(ABC):

    @abstractmethod
    def insert_video(self, data: Dict):
        pass