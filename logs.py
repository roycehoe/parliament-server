import logging
import sys
from types import FrameType
from typing import cast

from loguru import logger

FASTAPI_LOGGERS = ("uvicorn.asgi", "uvicorn.access")
DEFAULT_LOGGING_LEVEL = logging.INFO


class LogsInterceptor(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level,
            record.getMessage(),
        )


def get_configured_logging():
    logging.getLogger().handlers = [LogsInterceptor()]
    for fastapi_logger in FASTAPI_LOGGERS:
        logging.getLogger(fastapi_logger).handlers = [
            LogsInterceptor(level=DEFAULT_LOGGING_LEVEL)
        ]

    logger.configure(handlers=[{"sink": sys.stderr, "level": DEFAULT_LOGGING_LEVEL}])
