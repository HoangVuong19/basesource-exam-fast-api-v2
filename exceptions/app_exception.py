from exceptions.base_exception import BaseException
from utils.messages import load_messages

messages = load_messages()


class AppException(BaseException):
    def __init__(self, error_code: str, rollback: bool = False):
        self.http_code = 200
        self.error_code = error_code
        self.message = messages["APP_EXCEPTION"].get(error_code, "Application error!")
        self.rollback = rollback
