# ReStocker

Утилитарное приложение для учёта товаров и расходников в малых магазинах и мастерских.

## Структура проекта

```
ReStocker/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── core/        # Конфигурация и БД
│   │   ├── models/      # SQLAlchemy модели
│   │   ├── schemas/     # Pydantic схемы
│   │   ├── services/    # Бизнес-логика
│   │   ├── integrations/# Интеграции с CRM
│   │   └── utils/       # Утилиты
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/            # Telegram Mini App
│   ├── src/
│   │   ├── components/  # UI компоненты
│   │   ├── pages/       # Страницы приложения
│   │   ├── services/    # API клиент
│   │   └── utils/       # Утилиты
│   └── public/
│
└── PROJECT.md          # Полная инструкция проекта
```

## Установка

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
cp .env.example .env
# Настройте .env файл
```

### Frontend

```bash
cd frontend
npm install
```

## Запуск

### Backend

```bash
cd backend
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm run dev
```

## Разработка

Следуйте инструкциям в `PROJECT.md` для понимания архитектуры и требований проекта.

