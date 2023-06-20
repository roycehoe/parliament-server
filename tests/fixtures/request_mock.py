import pytest
import requests


@pytest.fixture
def hansard_API_raises_http_error(monkeypatch):
    def mock_hansard_API_raises_http_error(*args, **kwargs):
        raise requests.HTTPError

    monkeypatch.setattr("requests.post", mock_hansard_API_raises_http_error)


@pytest.fixture
def hansard_API_raises_request_exception(monkeypatch):
    def mock_hansard_API_raises_request_exception(*args, **kwargs):
        raise requests.RequestException

    monkeypatch.setattr("requests.post", mock_hansard_API_raises_request_exception)


@pytest.fixture
def hansard_API_raises_unexpected_exception(monkeypatch):
    def mock_hansard_API_raises_unexpected_exception(*args, **kwargs):
        raise Exception

    monkeypatch.setattr("requests.post", mock_hansard_API_raises_unexpected_exception)
