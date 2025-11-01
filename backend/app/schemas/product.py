"""
Pydantic схемы для товара/расходника
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProductBase(BaseModel):
    """Базовая схема товара"""
    name: str
    category: Optional[str] = None
    unit: str = "шт"
    quantity: float = 0.0
    threshold: float = 0.0


class ProductCreate(ProductBase):
    """Схема для создания товара"""
    pass


class ProductUpdate(BaseModel):
    """Схема для обновления товара"""
    name: Optional[str] = None
    category: Optional[str] = None
    unit: Optional[str] = None
    quantity: Optional[float] = None
    threshold: Optional[float] = None


class ProductResponse(ProductBase):
    """Схема для ответа с данными товара"""
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True

