"""
API endpoints для кнопок "одно действие"
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db

router = APIRouter()


@router.get("/")
async def get_buttons(db: Session = Depends(get_db)):
    """Получить список кнопок"""
    # TODO: реализовать логику
    return []


@router.post("/")
async def create_button(db: Session = Depends(get_db)):
    """Создать кнопку"""
    # TODO: реализовать логику
    return {}


@router.post("/{button_id}/execute")
async def execute_button(button_id: int, db: Session = Depends(get_db)):
    """Выполнить списание по кнопке"""
    # TODO: реализовать логику
    return {}


@router.delete("/{button_id}")
async def delete_button(button_id: int, db: Session = Depends(get_db)):
    """Удалить кнопку"""
    # TODO: реализовать логику
    return {}

