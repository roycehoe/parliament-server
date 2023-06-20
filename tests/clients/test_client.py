import pytest
import requests
from clients.hansard import get_hansard_API_response
from constants import HANSARD_BASE_URL
from exceptions import HansardAPICallException
from tests.fixtures.request_mock import (
    hansard_API_raises_http_error,
    hansard_API_raises_request_exception,
)


def test_get_hansard_API_response_success(requests_mock):
    mock_response = {"key": "value"}
    url = f"{HANSARD_BASE_URL}?sittingDate=2023-06-19"
    requests_mock.post(url, json=mock_response, status_code=200)

    response = get_hansard_API_response("2023-06-19")
    assert response.json() == mock_response


def test_get_hansard_API_response_http_error(hansard_API_raises_http_error):
    with pytest.raises(HansardAPICallException):
        get_hansard_API_response("2023-06-19")


def test_get_hansard_API_response_request_exception(
    hansard_API_raises_request_exception,
):
    with pytest.raises(HansardAPICallException):
        get_hansard_API_response("2023-06-19")


def test_get_hansard_API_response_unexpected_exception(
    hansard_API_raises_request_exception,
):
    with pytest.raises(HansardAPICallException):
        get_hansard_API_response("2023-06-19")
