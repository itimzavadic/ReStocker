"""
Pydantic схемы для валидации данных
"""
from app.schemas.user import UserBase, UserCreate, UserUpdate, UserResponse
from app.schemas.product import ProductBase, ProductCreate, ProductUpdate, ProductResponse
from app.schemas.rule import (
    RuleBase, RuleCreate, RuleUpdate, RuleResponse,
    RuleItemBase, RuleItemCreate, RuleItemResponse
)
from app.schemas.button import (
    ManualButtonBase, ManualButtonCreate, ManualButtonUpdate, ManualButtonResponse,
    ManualButtonItemBase, ManualButtonItemCreate, ManualButtonItemResponse
)
from app.schemas.sales_log import SalesLogBase, SalesLogCreate, SalesLogResponse

__all__ = [
    # User schemas
    "UserBase",
    "UserCreate",
    "UserUpdate",
    "UserResponse",
    # Product schemas
    "ProductBase",
    "ProductCreate",
    "ProductUpdate",
    "ProductResponse",
    # Rule schemas
    "RuleBase",
    "RuleCreate",
    "RuleUpdate",
    "RuleResponse",
    "RuleItemBase",
    "RuleItemCreate",
    "RuleItemResponse",
    # Button schemas
    "ManualButtonBase",
    "ManualButtonCreate",
    "ManualButtonUpdate",
    "ManualButtonResponse",
    "ManualButtonItemBase",
    "ManualButtonItemCreate",
    "ManualButtonItemResponse",
    # SalesLog schemas
    "SalesLogBase",
    "SalesLogCreate",
    "SalesLogResponse",
]
