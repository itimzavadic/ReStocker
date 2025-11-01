"""
Функции безопасности и авторизации
"""
from fastapi import HTTPException, status, Header, Depends
from sqlalchemy.orm import Session
from typing import Optional

from app.core.database import get_db
from app.models.user import User
from app.utils.telegram_auth import verify_telegram_webapp_data


async def get_current_user(init_data: str = None):
    """
    Получить текущего пользователя из Telegram WebApp данных
    
    TODO: Реализовать проверку авторизации через Telegram
    """
    if not init_data:
        return None
    
    user_data = verify_telegram_webapp_data(init_data)
    return user_data


def get_current_user_id(
    db: Session = Depends(get_db),
    x_telegram_id: Optional[int] = Header(None, alias="X-Telegram-Id")
) -> int:
    """
    Получить или создать пользователя по telegram_id
    
    Временное решение для разработки. Использует заголовок X-Telegram-Id.
    
    TODO: Заменить на полноценную авторизацию через Telegram WebApp Data
    """
    if not x_telegram_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Telegram ID is required. Provide X-Telegram-Id header"
        )
    
    # Ищем существующего пользователя
    user = db.query(User).filter(User.telegram_id == x_telegram_id).first()
    
    if not user:
        # Создаем нового пользователя (для разработки)
        user = User(
            telegram_id=x_telegram_id,
            name=f"User {x_telegram_id}"
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    return user.id


def get_current_user_db(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
) -> User:
    """
    Получить объект пользователя из базы данных
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
