"""
Главный роутер API v1
"""
from fastapi import APIRouter

from app.api.v1.endpoints import products, buttons, rules, logs, webhooks

api_router = APIRouter()

api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(buttons.router, prefix="/buttons", tags=["buttons"])
api_router.include_router(rules.router, prefix="/rules", tags=["rules"])
api_router.include_router(logs.router, prefix="/logs", tags=["logs"])
api_router.include_router(webhooks.router, prefix="/webhooks", tags=["webhooks"])

