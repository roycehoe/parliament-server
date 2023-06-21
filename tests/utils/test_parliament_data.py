import logging
import time

import pytest

from exceptions import HansardAPICallException
from utils.parliament_data import _retry, get_parliament_data


# Mock function for testing purposes
def mock_function():
    return "Success"


# Mock function that always raises an exception
def mock_function_with_exception():
    raise ValueError("Mock Exception")

