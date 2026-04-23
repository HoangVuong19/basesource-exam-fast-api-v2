from sqlalchemy import Boolean, Column, Integer, String

from models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
