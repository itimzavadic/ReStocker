"""
API endpoints для правил списания
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def get_rules(db: Session = Depends(get_db)):
    """Получить список правил"""
    # TODO: реализовать логику
    return []


@router.post("/")
async def create_rule(db: Session = Depends(get_db)):
    """Создать правило"""
    # TODO: реализовать логику
    return {}


@router.delete("/{rule_id}")
async def delete_rule(rule_id: int, db: Session = Depends(get_db)):
    """Удалить правило"""
    # TODO: реализовать логику
    return {}

