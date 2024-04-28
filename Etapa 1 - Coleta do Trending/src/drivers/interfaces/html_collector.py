'''INTERFACE: Coletar informções relevantes do HTML'''
from abc import ABC
from abc import abstractmethod

class HtmlCollectorInterface(ABC):
    @abstractmethod
    def collect_essential_information(self, html: str):
        pass
