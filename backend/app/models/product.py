"""
Модель товара/расходника
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class Product(Base):
    """Модель товара/расходника"""
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    category = Column(String, nullable=True, index=True)
    unit = Column(String, nullable=False, default="шт")  # единица измерения
    quantity = Column(Float, default=0.0)  # остаток
    threshold = Column(Float, default=0.0)  # порог
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Связи
    owner = relationship("User", back_populates="products")
    rule_items = relationship("RuleItem", back_populates="product")
    button_items = relationship("ManualButtonItem", back_populates="product")
    sales_logs = relationship("SalesLog", back_populates="product")

