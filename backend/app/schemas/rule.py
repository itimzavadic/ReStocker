"""
Pydantic схемы для правил списания
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

from app.models.rule import TriggerType


class RuleItemBase(BaseModel):
    """Базовая схема элемента правила"""
    product_id: int
    quantity: float


class RuleItemCreate(RuleItemBase):
    """Схема для создания элемента правила"""
    pass


class RuleItemResponse(RuleItemBase):
    """Схема для ответа с данными элемента правила"""
    id: int
    rule_id: int

    class Config:
        from_attributes = True


class RuleBase(BaseModel):
    """Базовая схема правила"""
    trigger_type: TriggerType
    trigger_value: str
    items: List[RuleItemCreate] = []


class RuleCreate(RuleBase):
    """Схема для создания правила"""
    pass


class RuleUpdate(BaseModel):
    """Схема для обновления правила"""
    trigger_type: Optional[TriggerType] = None
    trigger_value: Optional[str] = None
    items: Optional[List[RuleItemCreate]] = None


class RuleResponse(BaseModel):
    """Схема для ответа с данными правила"""
    id: int
    trigger_type: TriggerType
    trigger_value: str
    owner_id: int
    created_at: datetime
    items: List[RuleItemResponse] = []

    class Config:
        from_attributes = True

