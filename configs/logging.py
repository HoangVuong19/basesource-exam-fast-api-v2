import logging
from logging.handlers import TimedRotatingFileHandler
import os

from configs.enums import Environment
from configs.context import get_request_id
from configs.env import get_settings


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        s = super().format(record)
        if record:
            s = s.replace("\r\n", "").replace("\n", "")
        return s


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = get_request_id()
        return True


def setup_logging():
    settings = get_settings()

    level = logging.DEBUG if settings.environment == Environment.local else logging.INFO

    formatter = OneLineExceptionFormatter(
        "%(asctime)-15s - %(request_id)s - %(name)-5s - %(levelname)s - [%(filename)s:%(lineno)s - %(funcName)s() ] - %(message)s"
    )

    # ===== ROOT LOGGER =====
    logger = logging.getLogger()
    logger.setLevel(level)

    if logger.handlers:
        return

    # console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.addFilter(ContextFilter())
    logger.addHandler(console_handler)

    # file logging (local)
    if settings.environment == Environment.local and settings.log_file_path:
        os.makedirs(settings.log_file_path, exist_ok=True)

        log_file = os.path.join(
            settings.log_file_path,
            f"{settings.app_name}.log",
        )

        file_handler = TimedRotatingFileHandler(
            filename=log_file,
            when="midnight",
            encoding="utf-8",
            backupCount=14,
        )
        file_handler.setFormatter(formatter)
        file_handler.addFilter(ContextFilter())

        logger.addHandler(file_handler)

    # ===== SQL LOGGER =====
    sql_logger = logging.getLogger("sqlalchemy.engine.Engine")
    sql_logger.setLevel(logging.INFO)

    # propagate into root logger
    sql_logger.propagate = True
