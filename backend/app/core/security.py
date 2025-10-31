"""
Функции безопасности и авторизации
"""
from app.utils.telegram_auth import verify_telegram_webapp_data


async def get_current_user(init_data: str = None):
    """
    Получить текущего пользователя из Telegram WebApp данных
    
    TODO: Реализовать проверку авторизации через Telegram
    """
    if not init_data:
        return None
    
    user_data = verify_telegram_webapp_data(init_data)
    return user_data

