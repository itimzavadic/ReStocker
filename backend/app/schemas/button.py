"""
Pydantic схемы для кнопок "одно действие"
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class ManualButtonItemBase(BaseModel):
    """Базовая схема элемента кнопки"""
    product_id: int
    quantity: float


class ManualButtonItemCreate(ManualButtonItemBase):
    """Схема для создания элемента кнопки"""
    pass


class ManualButtonItemResponse(ManualButtonItemBase):
    """Схема для ответа с данными элемента кнопки"""
    id: int
    button_id: int

    class Config:
        from_attributes = True


class ManualButtonBase(BaseModel):
    """Базовая схема кнопки"""
    name: str
    items: List[ManualButtonItemCreate] = []


class ManualButtonCreate(ManualButtonBase):
    """Схема для создания кнопки"""
    pass


class ManualButtonUpdate(BaseModel):
    """Схема для обновления кнопки"""
    name: Optional[str] = None
    items: Optional[List[ManualButtonItemCreate]] = None


class ManualButtonResponse(BaseModel):
    """Схема для ответа с данными кнопки"""
    id: int
    name: str
    owner_id: int
    created_at: datetime
    items: List[ManualButtonItemResponse] = []

    class Config:
        from_attributes = True

