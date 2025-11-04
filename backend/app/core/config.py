"""
Конфигурация приложения
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    """Настройки приложения"""
    
    # База данных
    DATABASE_URL: str = "sqlite:///restocker.db"
    
    # Telegram Bot
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_SECRET_KEY: str = ""
    
    # CORS
    CORS_ORIGINS: List[str] = ["https://web.telegram.org", "https://df094aa7b7b527.lhr.life", "https://fcc85d962b95bc.lhr.life", "http://localhost:3000"]
    
    # API
    API_V1_PREFIX: str = "/api/v1"
    
    # Подписки
    TRIAL_PERIOD_DAYS: int = 14
    PREMIUM_PRICE: float = 5.0
    
    # pydantic-settings v2 configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra='allow',
    )


settings = Settings()

