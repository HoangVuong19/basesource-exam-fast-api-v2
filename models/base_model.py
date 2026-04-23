from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.orm import declarative_base
from typing import TypeVar

Base = declarative_base()
ModelType = TypeVar("ModelType", bound=Base)  # type: ignore


class BaseModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    created_by = Column(String(255))
    updated_at = Column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now()
    )
    updated_by = Column(String(255))
