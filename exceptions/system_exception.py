from exceptions.base_exception import BaseException
from utils.messages import load_messages

messages = load_messages()


class SystemException(BaseException):

    def __init__(self, error_code: str = "exam500", rollback: bool = True):
        self.http_code = 500
        self.error_code = error_code
        self.message = messages["SYSTEM_EXCEPTION"].get(error_code, "System error!")
        self.rollback = rollback
