from .http_requester imoprt HttpRequester

def test_set_urls():
    http_requester = HttpRequester()

    print(http_requester.urls)