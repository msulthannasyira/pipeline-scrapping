import pytest
from utils.extract import fetch_page

def test_fetch_page_success():
    url = "https://fashion-studio.dicoding.dev"
    soup = fetch_page(url)
    assert soup is not None
    assert soup.title is not None

def test_fetch_page_fail(monkeypatch):
    def mock_requests_get(*args, **kwargs):
        class MockResponse:
            status_code = 404
        return MockResponse()
    
    from utils import extract
    monkeypatch.setattr("utils.extract.requests.get", mock_requests_get)

    url = "https://invalid-url.com"
    soup = extract.fetch_page(url)
    assert soup is None

