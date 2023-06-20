import json

from crud.parliament_data import crud_parliament_data
from crud.parliament_dates import crud_parliament_dates
from crud.redis import CRUDRedis, crud_redis
from exceptions import (
    CorruptedParliamentDataFileWriteException,
    CorruptedParliamentDateFileReadException,
    DateRangeException,
    EmptyParliamentDateFileException,
    HansardAPICallException,
    NoParliamentDataFileException,
)
from fastapi import HTTPException
from utils.parliament_data import get_parliament_data
from utils.parliament_dates import get_parliament_sitting_dates


def _get_missing_parliament_dates() -> list[str]:
    try:
        date_after_last_saved_parliament_date = (
            crud_parliament_dates.day_after_last_saved()
        )
    except EmptyParliamentDateFileException:
        crud_parliament_dates.create()
        date_after_last_saved_parliament_date = (
            crud_parliament_dates.day_after_last_saved()
        )

    except CorruptedParliamentDateFileReadException:
        raise HTTPException(500, "Something went wrong")
    except PermissionError:
        raise HTTPException(500, "Something went wrong")

    try:
        return get_parliament_sitting_dates(date_after_last_saved_parliament_date)
    except DateRangeException:
        raise HTTPException(500, "Something went wrong")


def prepopulate_missing_parliament_data() -> None:
    try:
        missing_parliament_dates = _get_missing_parliament_dates()
    except EmptyParliamentDateFileException:
        raise HTTPException(500, "Something went wrong")
    except CorruptedParliamentDateFileReadException:
        raise HTTPException(500, "Something went wrong")
    except PermissionError:
        raise HTTPException(500, "Something went wrong")
    except DateRangeException:
        raise HTTPException(500, "Something went wrong")

    try:
        crud_parliament_dates.append(missing_parliament_dates)
    except PermissionError:
        raise HTTPException(500, "Something went wrong")
    except CorruptedParliamentDateFileReadException:
        raise HTTPException(500, "Something went wrong")

    for missing_parliament_date in missing_parliament_dates:
        try:
            parliament_data = get_parliament_data(missing_parliament_date)
        except HansardAPICallException:
            raise HTTPException(500, "Something went wrong")

        try:
            crud_parliament_data.create(missing_parliament_date, parliament_data)
        except PermissionError:
            raise HTTPException(500, "Something went wrong")
        except CorruptedParliamentDataFileWriteException:
            raise HTTPException(500, "Something went wrong")


def load_parliament_data(crud_redis: CRUDRedis):
    try:
        parliament_dates = crud_parliament_dates.get_all()
    except NoParliamentDataFileException:
        raise HTTPException(500, "Something went wrong")
    except PermissionError:
        raise HTTPException(500, "Something went wrong")
    except CorruptedParliamentDateFileReadException:
        raise HTTPException(500, "Something went wrong")

    for parliament_date in parliament_dates:
        try:
            parliament_data = crud_parliament_data.get(parliament_date)
        except NoParliamentDataFileException:
            raise HTTPException(500, "Something went wrong")
        except PermissionError:
            raise HTTPException(500, "Something went wrong")
        except CorruptedParliamentDateFileReadException:
            raise HTTPException(500, "Something went wrong")
        crud_redis.create(parliament_date, json.dumps(parliament_data))


def prepopulate_parliament_data():
    prepopulate_missing_parliament_data()
    load_parliament_data(crud_redis)
