"""
Pydantic схемы для журнала операций
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.models.sales_log import ActionType, SourceType


class SalesLogBase(BaseModel):
    """Базовая схема журнала"""
    action: ActionType
    product_id: int
    quantity: float
    source: SourceType
    source_details: Optional[str] = None


class SalesLogCreate(SalesLogBase):
    """Схема для создания записи в журнале"""
    pass


class SalesLogResponse(SalesLogBase):
    """Схема для ответа с данными журнала"""
    id: int
    datetime: datetime
    user_id: int

    class Config:
        from_attributes = True

