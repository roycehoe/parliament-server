import json
from dataclasses import dataclass
from datetime import date, datetime, timedelta

from constants import (
    DEFAULT_DATETIME_FORMAT,
    FIRST_PARLIAMENT_SITTING,
    PATH_TO_PARLIAMENT_SITTING_DATES,
)
from exceptions import (
    CorruptedParliamentDateFileReadException,
    CorruptedParliamentDateFileWriteException,
    EmptyParliamentDateFileException,
    NoParliamentDateFileException,
)
from utils.date import get_date_from_ddmmyyyy


@dataclass
class CRUDParliamentDates:
    path: str = PATH_TO_PARLIAMENT_SITTING_DATES

    def get_all(self) -> list[str]:
        try:
            with open(self.path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise NoParliamentDateFileException
        except PermissionError:
            raise PermissionError
        except json.JSONDecodeError:
            raise CorruptedParliamentDateFileReadException

    def create(self) -> None:
        with open(self.path, "w") as file:
            first_parliament_sitting = date(*FIRST_PARLIAMENT_SITTING).strftime(
                DEFAULT_DATETIME_FORMAT
            )
            json.dump([first_parliament_sitting], file)

    def append(self, new_dates: list[str]) -> None:
        try:
            with open(self.path, "r") as file:
                old_parliament_dates = json.load(file)
        except json.JSONDecodeError:
            raise CorruptedParliamentDateFileReadException

        try:
            with open(self.path, "w") as file:
                new_data = [*old_parliament_dates, *new_dates]
                json.dump(new_data, file)
        except PermissionError:
            raise PermissionError
        except json.JSONDecodeError:
            raise CorruptedParliamentDateFileWriteException

    def day_after_last_saved(self) -> date:
        try:
            with open(self.path, "r") as file:
                last_saved_day = get_date_from_ddmmyyyy(json.load(file)[-1])
                day_after_last_saved = last_saved_day + timedelta(days=1)
                return day_after_last_saved
        except IndexError:
            raise EmptyParliamentDateFileException
        except TypeError:
            raise CorruptedParliamentDateFileReadException
        except PermissionError:
            raise PermissionError
        except json.JSONDecodeError:
            raise CorruptedParliamentDateFileReadException


crud_parliament_dates = CRUDParliamentDates()
