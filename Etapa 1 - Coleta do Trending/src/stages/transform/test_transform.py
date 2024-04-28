from src.stages.extract.extract_html import ExtractHtml
from src.stages.transform.transform_html import TransformHtml
from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector


def test_transform():
    extract_data = ExtractHtml(HttpRequester(), HtmlCollector())
    
    extract_contract = extract_data.extract()
    transform_html = TransformHtml()
    transform_contract = transform_html.transform(extract_contract)
    print(transform_contract[0])
