from src.drivers.interfaces.http_requester import HttpRequesterInterface
from src.errors.extract_error import ExtractionError

class ExtractHtml:
    def __init__(self, http_requester: HttpRequesterInterface) -> None:
        self.__http_requester = http_requester

    def extract(self):
        try:
            urls = self.__http_requester.set_urls()
            self.__http_requester.request_from_pages(urls)

        except Exception as exception:
            raise ExtractionError(str(exception)) from exception