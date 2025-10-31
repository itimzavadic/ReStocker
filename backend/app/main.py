"""
ReStocker Backend - FastAPI приложение
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.api import api_router

app = FastAPI(
    title="ReStocker API",
    description="API для учёта товаров и расходников",
    version="1.0.0"
)

# Настройка CORS для Telegram Mini App
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение API роутера
app.include_router(api_router, prefix=settings.API_V1_PREFIX)


@app.get("/")
async def root():
    return {"message": "ReStocker API", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}

