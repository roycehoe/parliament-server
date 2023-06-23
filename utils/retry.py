import time
from functools import wraps
from typing import Callable, Type, Union

from loguru import logger


def retry_request(
    exception_to_check: Type[Exception],
    log: str,
    tries: int = 4,
    delay: Union[int, float] = 3,
    backoff: Union[int, float] = 2,
) -> Callable:
    def deco_retry(f: Callable) -> Callable:
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 0:
                try:
                    return f(*args, **kwargs)
                except exception_to_check:
                    logger.warning(f"{log}")
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
                if mtries == 0:
                    raise exception_to_check

        return f_retry

    return deco_retry
