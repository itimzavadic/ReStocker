"""
API endpoints для вебхуков от CRM
"""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.database import get_db

router = APIRouter()


@router.post("/crm/{crm_name}")
async def receive_webhook(crm_name: str, request: Request, db: Session = Depends(get_db)):
    """Получить вебхук от CRM"""
    # TODO: реализовать логику обработки вебхуков
    data = await request.json()
    return {"status": "received", "crm": crm_name}

