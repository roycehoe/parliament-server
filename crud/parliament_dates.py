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
                day_after_last_saved = json.load(file)[-1] + timedelta(days=1)
                return datetime.strptime(
                    day_after_last_saved, DEFAULT_DATETIME_FORMAT
                ).date()
        except IndexError:
            raise EmptyParliamentDateFileException
        except TypeError:
            raise CorruptedParliamentDateFileReadException
        except PermissionError:
            raise PermissionError
        except json.JSONDecodeError:
            raise CorruptedParliamentDateFileReadException


crud_parliament_dates = CRUDParliamentDates()
