from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Callable

from clients.hansard import get_hansard_API_response
from constants import DEFAULT_DATETIME_FORMAT, FIRST_PARLIAMENT_SITTING
from exceptions import DateRangeException, HansardAPICallException
from loguru import logger


def _get_hansard_URL_formatted_dates(
    func: Callable,
) -> Callable[..., list[str]]:
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return [datetime.strftime(date, DEFAULT_DATETIME_FORMAT) for date in result]

    return wrap


@_get_hansard_URL_formatted_dates
def get_date_range(start: date, end: date) -> list[date]:
    delta = end - start
    if delta.days < 0:
        raise DateRangeException("End date must be before start date")
    return [start + timedelta(days=i) for i in range(delta.days + 1)]


def is_valid_parliament_sitting_date(date: str) -> bool:
    try:
        get_hansard_API_response(date)
        return True
    except HansardAPICallException:
        return False


def get_parliament_sitting_dates(
    start_date: date = date(*FIRST_PARLIAMENT_SITTING), end_date: date = date.today()
) -> list[str]:
    try:
        date_range = get_date_range(start_date, end_date)
    except DateRangeException:
        raise DateRangeException("End date must be before start date")

    parliament_sitting_dates = []
    for i in range(len(date_range)):
        logger.info(f"{i}/{len(date_range)}")
        if not is_valid_parliament_sitting_date(date_range[i]):
            continue
        parliament_sitting_dates.append(date_range[i])

    return parliament_sitting_dates
