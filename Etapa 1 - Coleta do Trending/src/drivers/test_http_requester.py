'''Testes para classe HtmlRequester'''
from src.drivers.http_requester import HttpRequester

def test_request_from_page():
    html_requester = HttpRequester()
    reponse = html_requester.request_from_page()
    print(reponse)
