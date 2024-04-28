from abc import ABC
from abc import abstractmethod

class HtmlCollectorInterface(ABC):
    @abstractmethod
    def collect_essential_information(cls, html: str):
        pass