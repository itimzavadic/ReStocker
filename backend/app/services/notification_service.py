"""
Сервис для отправки уведомлений в Telegram
"""
import httpx
from app.core.config import settings


class NotificationService:
    """Сервис для отправки уведомлений"""
    
    @staticmethod
    async def send_low_stock_notification(
        product_name: str,
        current_quantity: float,
        threshold: float,
        telegram_user_id: int
    ):
        """
        Отправить уведомление о низком остатке
        
        Args:
            product_name: название товара
            current_quantity: текущее количество
            threshold: пороговое значение
            telegram_user_id: ID пользователя в Telegram
        """
        # TODO: реализовать отправку уведомления через Telegram Bot API
        message = (
            f"⚠️ Низкий остаток!\n"
            f"Товар: {product_name}\n"
            f"Остаток: {current_quantity}\n"
            f"Порог: {threshold}"
        )
        pass

