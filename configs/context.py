# context.py
import uuid
from contextvars import ContextVar

request_id_ctx: ContextVar[uuid.UUID | None] = ContextVar("request_id", default=None)


def set_request_id(request_id: uuid.UUID):
    request_id_ctx.set(request_id)


def get_request_id() -> uuid.UUID | None:
    return request_id_ctx.get()
