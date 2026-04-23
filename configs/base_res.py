import humps
from pydantic import BaseModel


def to_camel(string: str) -> str:
    return humps.camelize(string)


class BaseResSchema(BaseModel):
    model_config = {
        "alias_generator": to_camel,
        "populate_by_name": True,
    }
