"""
Конфигурация приложения
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Настройки приложения"""
    
    # База данных
    DATABASE_URL: str = "postgresql://user:password@localhost/restocker"
    
    # Telegram Bot
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_SECRET_KEY: str = ""
    
    # CORS
    CORS_ORIGINS: List[str] = ["https://web.telegram.org"]
    
    # API
    API_V1_PREFIX: str = "/api/v1"
    
    # Подписки
    TRIAL_PERIOD_DAYS: int = 14
    PREMIUM_PRICE: float = 5.0
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

