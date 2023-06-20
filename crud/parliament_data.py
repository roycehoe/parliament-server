import json
from dataclasses import dataclass

from constants import PATH_TO_PARLIAMENT_DATA_DIR
from exceptions import (
    CorruptedParliamentDataFileReadException,
    CorruptedParliamentDataFileWriteException,
    NoParliamentDataFileException,
)


@dataclass
class CRUDParliamentData:
    dir: str = PATH_TO_PARLIAMENT_DATA_DIR

    def get(self, date: str) -> list[str]:
        try:
            with open(f"{self.dir}/{date}.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            raise NoParliamentDataFileException
        except PermissionError:
            raise PermissionError
        except json.JSONDecodeError:
            raise CorruptedParliamentDataFileReadException

    def create(self, date: str, parliament_data: dict) -> None:
        try:
            with open(f"{self.dir}/{date}.json", "w") as file:
                json.dump(parliament_data, file)
        except PermissionError:
            raise PermissionError
        except json.JSONDecodeError:
            raise CorruptedParliamentDataFileWriteException


crud_parliament_data = CRUDParliamentData()
