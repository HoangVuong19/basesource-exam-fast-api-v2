from fastapi import Request
from fastapi.exceptions import RequestValidationError

from configs.logging import logging
from exceptions.validation_exception import ValidationException
from utils.response import response_fail

logger = logging.getLogger(__name__)


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error("Validation error occurred", exc_info=True)
    err = exc.errors()[0]
    message = f"{err['loc'][-1]}: {err['msg']}"
    return response_fail(ValidationException("exam422", message))
