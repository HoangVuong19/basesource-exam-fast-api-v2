from exceptions.base_exception import BaseException
from utils.messages import load_messages

messages = load_messages()


class ValidationException(BaseException):
    def __init__(self, error_code: str, message: str):
        self.http_code = 200
        self.error_code = error_code
        self.message = message
