"""
API endpoints для товаров/расходников
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def get_products(db: Session = Depends(get_db)):
    """Получить список товаров"""
    # TODO: реализовать логику
    return []


@router.post("/")
async def create_product(db: Session = Depends(get_db)):
    """Создать товар"""
    # TODO: реализовать логику
    return {}


@router.put("/{product_id}")
async def update_product(product_id: int, db: Session = Depends(get_db)):
    """Обновить товар"""
    # TODO: реализовать логику
    return {}


@router.delete("/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    """Удалить товар"""
    # TODO: реализовать логику
    return {}

