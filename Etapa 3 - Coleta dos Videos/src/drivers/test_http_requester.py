from .http_requester import HttpRequester
from .html_collector import HtmlCollector
from src.infra.mocks.mock_database_repository import mock_select_channel

# def test_set_urls():
#     http_requester = HttpRequester()
#     urls = http_requester.set_urls()
#     print(urls)

def test_request_from_pages():
    html_collector = HtmlCollector
    http_requester = HttpRequester(html_collector)
    http_requester.request_from_pages(mock_select_channel)
