from sqlalchemy import Column, Float, Integer, String

from models.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    price = Column(Float)
    category_id = Column(Integer, nullable=False)
