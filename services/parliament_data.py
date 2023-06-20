import json

from crud.parliament_dates import crud_parliament_dates
from crud.redis import crud_redis
from exceptions import (
    CorruptedParliamentDateFileReadException,
    NoParliamentDateFileException,
)
from fastapi import HTTPException


def get_parliament_data(date: str) -> dict:
    if redis_data := crud_redis.get(date):
        try:
            return json.loads(redis_data)
        except json.JSONDecodeError:
            raise HTTPException(500, "Error reading parliament data")

    raise HTTPException(404, f"Parliament data not found")


def get_all_parliament_dates() -> list[str]:
    try:
        return crud_parliament_dates.get_all()

    except NoParliamentDateFileException:
        raise HTTPException(500, "No parliament dates found")
    except PermissionError:
        raise HTTPException(500, "Something went wrong")
    except CorruptedParliamentDateFileReadException:
        raise HTTPException(500, "Error reading parliament dates")
