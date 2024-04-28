from src.drivers.html_collector import HtmlCollector
from src.drivers.mocks.mock_http_requester import mock_http_html

def test_collect_essential_information():
    html_collector = HtmlCollector()
    html_collector.collect_essential_information(mock_http_html)