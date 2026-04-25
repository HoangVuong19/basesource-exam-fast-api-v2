from fastapi import Request
from fastapi.exceptions import RequestValidationError

from configs.logging import logging
from exceptions.validation_exception import ValidationException
from utils.response import response_fail

logger = logging.getLogger(__name__)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error("Validation error occurred", exc_info=True)
    message = " | ".join(
        [f"{'.'.join(map(str, err['loc']))}: {err['msg']}" for err in exc.errors()]
    )
    return response_fail(ValidationException("exam422", message))
