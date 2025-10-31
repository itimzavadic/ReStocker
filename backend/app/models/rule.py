"""
Модели правил списания
"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.core.database import Base


class TriggerType(str, enum.Enum):
    """Типы триггеров правил"""
    PRODUCT = "товар"
    CATEGORY = "категория"
    KEYWORD = "ключевое_слово"


class Rule(Base):
    """Модель правила списания"""
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    trigger_type = Column(Enum(TriggerType), nullable=False)
    trigger_value = Column(String, nullable=False)  # ID товара, название категории или ключевое слово
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Связи
    owner = relationship("User", back_populates="rules")
    items = relationship("RuleItem", back_populates="rule", cascade="all, delete-orphan")


class RuleItem(Base):
    """Элемент правила - связь правила с расходником и количеством"""
    __tablename__ = "rule_items"

    id = Column(Integer, primary_key=True, index=True)
    rule_id = Column(Integer, ForeignKey("rules.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Float, nullable=False)  # количество для списания
    
    # Связи
    rule = relationship("Rule", back_populates="items")
    product = relationship("Product", back_populates="rule_items")

