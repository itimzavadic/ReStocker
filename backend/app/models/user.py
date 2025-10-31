"""
Модель пользователя
"""
from sqlalchemy import Column, Integer, String, Enum, DateTime, BigInteger
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base


class UserRole(str, enum.Enum):
    """Роли пользователей"""
    MANAGER = "менеджер"
    OWNER = "владелец"


class SubscriptionType(str, enum.Enum):
    """Типы подписки"""
    FREE = "бесплатная"
    PREMIUM = "премиум"
    TRIAL = "пробная"


class User(Base):
    """Модель пользователя"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)
    role = Column(Enum(UserRole), default=UserRole.MANAGER)
    subscription = Column(Enum(SubscriptionType), default=SubscriptionType.TRIAL)
    telegram_id = Column(BigInteger, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Связи
    products = relationship("Product", back_populates="owner")
    rules = relationship("Rule", back_populates="owner")
    buttons = relationship("ManualButton", back_populates="owner")
    sales_logs = relationship("SalesLog", back_populates="user")

