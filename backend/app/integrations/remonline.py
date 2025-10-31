"""
Интеграция с RemOnline
"""
from app.integrations.base_crm import BaseCRMAdapter


class RemOnlineAdapter(BaseCRMAdapter):
    """Адаптер для RemOnline"""
    
    async def handle_webhook(self, data: dict) -> dict:
        # TODO: реализовать обработку вебхука RemOnline
        pass
    
    async def poll_sales(self) -> list:
        # TODO: реализовать опрос API RemOnline
        pass

