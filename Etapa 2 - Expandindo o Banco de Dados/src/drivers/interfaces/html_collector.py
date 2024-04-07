from abc import ABC, abstractmethod

class HtmlCollectorInterface(ABC):
    @abstractmethod
    def collect_essential_information(self, html: str) -> str:
        pass
    
