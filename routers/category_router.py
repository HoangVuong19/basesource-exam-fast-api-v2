from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from configs.database import get_db

from cruds import category_crud
from schemas.request.category_req import CategoryReq
from utils.response import response_success

router = APIRouter()


@router.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    crud = category_crud.CategoryCrud(db)
    return response_success(crud.get_all_categories())


@router.post("/categories")
def create_category(request: CategoryReq, db: Session = Depends(get_db)):
    crud = category_crud.CategoryCrud(db)
    return response_success(crud.create_category(request))
