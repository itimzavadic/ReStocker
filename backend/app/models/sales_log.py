"""
Модель журнала операций
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base


class ActionType(str, enum.Enum):
    """Типы действий"""
    WITHDRAWAL = "списание"
    ADDITION = "добавление"


class SourceType(str, enum.Enum):
    """Типы источников операций"""
    MANUAL = "ручное"
    CRM = "CRM"
    BUTTON = "кнопка"


class SalesLog(Base):
    """Модель журнала операций"""
    __tablename__ = "sales_logs"

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime, default=datetime.utcnow, index=True)
    action = Column(Enum(ActionType), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Float, nullable=False)
    source = Column(Enum(SourceType), nullable=False)
    source_details = Column(String, nullable=True)  # ID кнопки, название CRM и т.д.
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Связи
    product = relationship("Product", back_populates="sales_logs")
    user = relationship("User", back_populates="sales_logs")

