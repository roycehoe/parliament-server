from datetime import date, datetime

from constants import DEFAULT_DATETIME_FORMAT


def get_date_from_ddmmyyyy(
    date_string: str, format: str = DEFAULT_DATETIME_FORMAT
) -> date:
    return datetime.strptime(date_string, format).date()


def get_ddmmyyyy_from_date(date: date, format: str = DEFAULT_DATETIME_FORMAT) -> str:
    return date.strftime(format)
