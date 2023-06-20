import requests
from constants import HANSARD_BASE_URL
from exceptions import HansardAPICallException
from loguru import logger


def get_hansard_API_response(
    sitting_date: str, hansard_base_url=HANSARD_BASE_URL
) -> requests.Response:
    url = f"{hansard_base_url}?sittingDate={sitting_date}"
    try:
        return requests.post(url)
    except requests.HTTPError as e:
        logger.error(f"HTTP error occured during hansard API call: {e}")
        raise HansardAPICallException
    except requests.RequestException as e:
        logger.error(f"Request exception occured during hansard API call: {e}")
        raise HansardAPICallException
    except Exception as e:
        logger.error(f"Unexpected error occured during hansard API call: {e}")
        raise HansardAPICallException
