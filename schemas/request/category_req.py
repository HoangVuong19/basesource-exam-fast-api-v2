from pydantic import Field

from configs.base_req import BaseReqSchema


class CategoryReq(BaseReqSchema):
    name: str = Field(...)
    description: str = Field(None)
