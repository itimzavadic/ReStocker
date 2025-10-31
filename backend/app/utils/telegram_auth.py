"""
Утилиты для авторизации через Telegram WebApp
"""
import hashlib
import hmac
from typing import Optional
from app.core.config import settings


def verify_telegram_webapp_data(init_data: str) -> Optional[dict]:
    """
    Проверить подлинность данных от Telegram WebApp
    
    Args:
        init_data: строка с данными от Telegram WebApp
    
    Returns:
        Dict с данными пользователя или None если невалидно
    """
    # TODO: реализовать проверку подписи через Telegram WebApp Data
    # Используем settings.TELEGRAM_SECRET_KEY для проверки
    pass

