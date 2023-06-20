import time

from clients.hansard import get_hansard_API_response
from constants import HANSARD_API_MAX_RETRIES
from exceptions import HansardAPICallException
from loguru import logger


def _retry(func):
    def wrapper(*args, **kwargs):
        retries = 0
        while True:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                retries += 1
                logger.warning(
                    f"Failed to get hansard data. Attempt {retries}/{HANSARD_API_MAX_RETRIES}"
                )
                time.sleep(1)
                if retries <= HANSARD_API_MAX_RETRIES:
                    continue
                raise HansardAPICallException(e)

    return wrapper


@_retry
def get_parliament_data(sitting_date: str) -> dict:
    try:
        hansard_API_response = get_hansard_API_response(sitting_date)
        return hansard_API_response.json()
    except HansardAPICallException:
        raise HansardAPICallException
