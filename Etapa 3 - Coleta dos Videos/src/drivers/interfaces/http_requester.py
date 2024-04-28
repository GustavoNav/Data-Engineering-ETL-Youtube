from abc import ABC
from abc import abstractmethod

class HttpRequesterInterface(ABC):    
    @abstractmethod
    def request_from_pages(self, urls: list):
        pass
        
    @abstractmethod
    def set_urls(self):
        pass