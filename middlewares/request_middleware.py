import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from configs.context import get_request_id, set_request_id
from configs.logging import logging
from exceptions.app_exception import AppException
from exceptions.system_exception import SystemException
from utils.response import response_fail

logger = logging.getLogger(__name__)


class RequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # unique id for each request
        set_request_id(uuid.uuid4())
        request.state.request_id = get_request_id()

        logger.info(">>>>>> Start request")
        try:
            return await call_next(request)
        except AppException as e:
            return response_fail(e)
        except Exception as e:
            logger.exception(e)
            return response_fail(SystemException())
        finally:
            logger.info(">>>>>> End request")
