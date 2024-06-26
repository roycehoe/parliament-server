from clients.hansard import get_hansard_API_response
from exceptions import HansardAPICallException


def get_parliament_data(sitting_date: str) -> dict:
    try:
        hansard_API_response = get_hansard_API_response(sitting_date)
        return hansard_API_response.json()
    except HansardAPICallException:
        raise HansardAPICallException
