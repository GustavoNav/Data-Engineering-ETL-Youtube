from .html_collector import HtmlCollector
from .mocks.mock_html_requester import mock_html_requester

def test_collect_essential_information():
    html_collector = HtmlCollector()
    essential_information = html_collector.collect_essential_information(mock_html_requester)

    print(essential_information)