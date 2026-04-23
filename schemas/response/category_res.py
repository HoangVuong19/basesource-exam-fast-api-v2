from configs.base_res import BaseResSchema


class CategoryRes(BaseResSchema):
    id: int
    name: str
    description: str | None = None

    model_config = {"from_attributes": True}
