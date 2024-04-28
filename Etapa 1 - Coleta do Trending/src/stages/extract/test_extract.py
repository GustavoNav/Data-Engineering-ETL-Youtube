'''Teste da classe Extract'''
from src.drivers.http_requester import HtmlRequester
from src.drivers.html_collector import HtmlCollector
from src.stages.extract.extract_html import ExtractHtml
from src.contracts.extract_contract import ExtractContract

def test_extract():
    '''Testar função extract da Classe Extract'''
    extractor = ExtractHtml(http_requester=HtmlRequester(), html_collector=HtmlCollector())
    extract_cotract = extractor.extract()
    print(extract_cotract)
    assert isinstance(extract_cotract, ExtractContract)
