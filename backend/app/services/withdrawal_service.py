"""
Сервис для обработки списаний
"""
from sqlalchemy.orm import Session
from typing import List, Dict

from app.models.product import Product
from app.models.sales_log import SalesLog, ActionType, SourceType


class WithdrawalService:
    """Сервис для обработки списаний расходников"""
    
    @staticmethod
    async def withdraw_products(
        db: Session,
        withdrawals: List[Dict],  # [{"product_id": 1, "quantity": 2}, ...]
        source: SourceType,
        source_details: str = None,
        user_id: int = None
    ):
        """
        Списать расходники
        
        Args:
            db: сессия БД
            withdrawals: список словарей с product_id и quantity
            source: источник операции
            source_details: детали источника (ID кнопки, название CRM)
            user_id: ID пользователя
        """
        # TODO: реализовать логику списания
        # 1. Для каждого элемента withdrawals:
        #    - Получить продукт из БД
        #    - Уменьшить остаток
        #    - Проверить порог → отправить уведомление если нужно
        #    - Записать в журнал
        pass

