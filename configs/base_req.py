import humps
from pydantic import BaseModel, model_validator
from typing import Any


class BaseReqSchema(BaseModel):

    @model_validator(mode="before")
    @classmethod
    def convert_to_snake_case(cls, data: Any) -> Any:
        if isinstance(data, dict):
            return humps.decamelize(data)
        return data
