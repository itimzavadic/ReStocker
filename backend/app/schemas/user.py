"""
Pydantic схемы для пользователя
"""
from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional
import re

from app.models.user import UserRole, SubscriptionType


class UserBase(BaseModel):
    """Базовая схема пользователя"""
    name: str
    email: Optional[str] = None
    role: UserRole = UserRole.MANAGER
    telegram_id: int

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
            raise ValueError('Invalid email format')
        return v


class UserCreate(UserBase):
    """Схема для создания пользователя"""
    pass


class UserUpdate(BaseModel):
    """Схема для обновления пользователя"""
    name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[UserRole] = None
    subscription: Optional[SubscriptionType] = None

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
            raise ValueError('Invalid email format')
        return v


class UserResponse(UserBase):
    """Схема для ответа с данными пользователя"""
    id: int
    subscription: SubscriptionType
    created_at: datetime

    class Config:
        from_attributes = True

