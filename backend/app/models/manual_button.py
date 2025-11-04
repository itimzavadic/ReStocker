"""
Модели кнопок "одно действие"
"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


class ManualButton(Base):
    """Модель кнопки "одно действие" """
    __tablename__ = "manual_buttons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Связи
    owner = relationship("User", back_populates="buttons")
    items = relationship("ManualButtonItem", back_populates="button", cascade="all, delete-orphan")


class ManualButtonItem(Base):
    """Элемент кнопки - связь кнопки с расходником и количеством"""
    __tablename__ = "manual_button_items"

    id = Column(Integer, primary_key=True, index=True)
    button_id = Column(Integer, ForeignKey("manual_buttons.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Float, nullable=False)  # количество для списания
    
    # Связи
    button = relationship("ManualButton", back_populates="items")
    product = relationship("Product", back_populates="button_items")

