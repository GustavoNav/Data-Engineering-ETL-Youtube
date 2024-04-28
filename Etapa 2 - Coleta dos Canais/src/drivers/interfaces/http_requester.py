from abc import ABCMeta, abstractmethod
from src.drivers.html_collector import HtmlCollector

class HttpRequesterInterface(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.html_collector = HtmlCollector()

    @abstractmethod
    def request_from_pages(self, urls: list) -> None:
        pass

    @abstractmethod
    def set_urls(self) -> list:
        pass
