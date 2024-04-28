from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester

def test_collect_essential_information():
    html_requester = HttpRequester()
    html_collector = HtmlCollector()

    html = html_requester.request_from_page()['html']
    assert isinstance(html, str)

    essential_information = html_collector.collect_essential_information(html)
    for i in range(5):
        print(essential_information[i])
