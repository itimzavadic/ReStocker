"""
Базовый класс для интеграций с CRM
"""
from abc import ABC, abstractmethod
from typing import Dict, List


class BaseCRMAdapter(ABC):
    """Базовый адаптер для интеграции с CRM"""
    
    @abstractmethod
    async def handle_webhook(self, data: Dict) -> Dict:
        """
        Обработать вебхук от CRM
        
        Returns:
            Dict с информацией о продаже: {
                "product_id": int или None,
                "product_name": str,
                "category": str,
                "keywords": List[str]
            }
        """
        pass
    
    @abstractmethod
    async def poll_sales(self) -> List[Dict]:
        """
        Опросить API CRM на предмет новых продаж (для CRM без вебхуков)
        
        Returns:
            List[Dict] с информацией о продажах
        """
        pass

