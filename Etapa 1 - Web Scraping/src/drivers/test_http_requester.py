'''Testes para classe HtmlRequester'''
from .http_requester import HtmlRequester

def test_request_from_page():
    html_requester = HtmlRequester()
    reponse = html_requester.request_from_page()
    print(reponse)
