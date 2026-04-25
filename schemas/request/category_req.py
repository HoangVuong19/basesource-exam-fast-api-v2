from pydantic import Field

from configs.base_req import BaseReqSchema


class CategoryReq(BaseReqSchema):
    id: int = Field(None)
    name: str = Field(...)
    description: str = Field(None)
