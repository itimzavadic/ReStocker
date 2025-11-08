"""
Конфигурация приложения
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    """Настройки приложения"""
    
    # База данных
    # Railway автоматически предоставляет DATABASE_URL через переменную окружения
    DATABASE_URL: str = "sqlite:///restocker.db"
    
    # Telegram Bot
    TELEGRAM_BOT_TOKEN: str = ""
    TELEGRAM_SECRET_KEY: str = ""
    
    # CORS
    # Railway домен будет добавлен автоматически через переменную окружения RAILWAY_PUBLIC_DOMAIN
    CORS_ORIGINS: List[str] = ["https://web.telegram.org", "http://localhost:3000"]
    
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
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Автоматически добавляем Railway домен в CORS, если он доступен
        import os
        railway_domain = os.getenv("RAILWAY_PUBLIC_DOMAIN")
        if railway_domain:
            # Добавляем Railway домен в CORS
            if f"https://{railway_domain}" not in self.CORS_ORIGINS:
                self.CORS_ORIGINS.append(f"https://{railway_domain}")
        
        # Используем DATABASE_URL из переменной окружения, если доступен (Railway предоставляет PostgreSQL)
        db_url = os.getenv("DATABASE_URL")
        if db_url:
            # Railway предоставляет DATABASE_URL в формате postgresql://, но SQLAlchemy ожидает postgresql://
            # Конвертируем если нужно
            if db_url.startswith("postgres://"):
                db_url = db_url.replace("postgres://", "postgresql://", 1)
            self.DATABASE_URL = db_url


settings = Settings()

