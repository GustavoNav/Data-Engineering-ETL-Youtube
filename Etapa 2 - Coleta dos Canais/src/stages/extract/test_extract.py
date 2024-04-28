from src.stages.extract.extract_html import ExtractHtml
from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector


def test_extract():
    html_collector = HtmlCollector()
    http_requester = HttpRequester(html_collector)
    extractor = ExtractHtml(http_requester)
    extractor.extract()
