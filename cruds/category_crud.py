from sqlalchemy.orm import Session

from cruds.base_crud import BaseCrud
from models.category_model import Category
from schemas.request.category_req import CategoryReq
from schemas.response.category_res import CategoryRes


class CategoryCrud(BaseCrud[Category]):
    def __init__(self, db: Session):
        super().__init__(db)
        self.model = Category

    def get_all_categories(self) -> list[CategoryRes]:
        return [CategoryRes.model_validate(category) for category in self.get_all()]

    def create_category(self, req: CategoryReq) -> CategoryRes:
        return CategoryRes.model_validate(self.create(req.model_dump()))

    def update_category(self, req: CategoryReq) -> CategoryRes:
        return CategoryRes.model_validate(
            self.update(req.id, req.model_dump(exclude={"id"}))
        )

    def delete_category(self, category_id: int) -> str:
        self.delete_by_id(category_id, logical=False)
        return "Delete category successfully"
