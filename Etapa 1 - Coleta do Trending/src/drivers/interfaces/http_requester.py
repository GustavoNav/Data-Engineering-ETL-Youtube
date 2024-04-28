'''INTERFACE: Requisitar html da pagina.'''
from abc import ABC
from abc import abstractmethod

class HttpRequesterInterface(ABC):
    @abstractmethod
    def request_from_page(self):
        pass
