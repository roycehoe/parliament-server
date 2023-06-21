from datetime import date

import pytest

from utils.date import get_date_from_ddmmyyyy, get_ddmmyyyy_from_date


def test_get_date_from_ddmmyyyy():
    assert get_date_from_ddmmyyyy("21-06-2023") == date(2023, 6, 21)
    assert get_date_from_ddmmyyyy("19-06-2027") == date(2027, 6, 19)
    assert get_date_from_ddmmyyyy("23-06-2021", "%d-%m-%Y") == date(2021, 6, 23)
    assert get_date_from_ddmmyyyy("11/09/2001", "%d/%m/%Y") == date(2001, 9, 11)


def test_get_ddmmyyyy_from_date():
    assert get_ddmmyyyy_from_date(date(2023, 6, 21)) == "21-06-2023"
    assert get_ddmmyyyy_from_date(date(2021, 6, 23), "%d-%m-%Y") == "23-06-2021"
    assert get_ddmmyyyy_from_date(date(2023, 6, 21), "%m/%d/%Y") == "06/21/2023"


def test_get_date_from_ddmmyyyy_invalid_date():
    with pytest.raises(ValueError):
        get_date_from_ddmmyyyy("210623", "%Y-%m-%d")


def test_get_date_from_ddmmyyyy_invalid_format():
    with pytest.raises(ValueError):
        get_date_from_ddmmyyyy("210623", "tis' but a scratch")


def test_get_ddmmyyyy_from_date_invalid_format():
    assert (
        get_ddmmyyyy_from_date(date(2023, 6, 21), "tis' but a scratch")
        == "tis' but a scratch"
    )
