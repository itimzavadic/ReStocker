# Инструкция по деплою ReStocker на Railway

## Подготовка

### 1. Создайте аккаунт на Railway

1. Перейдите на [railway.app](https://railway.app)
2. Зарегистрируйтесь через GitHub
3. Подтвердите email

### 2. Подготовьте репозиторий GitHub

1. Создайте новый репозиторий на GitHub
2. Закоммитьте код:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/ваш-username/restocker.git
   git push -u origin main
   ```

## Деплой Backend

### Шаг 1: Создайте новый проект на Railway

1. В Railway Dashboard нажмите **"New Project"**
2. Выберите **"Deploy from GitHub repo"**
3. Выберите ваш репозиторий
4. Railway автоматически определит Python проект

### Шаг 2: Добавьте PostgreSQL базу данных

1. В проекте нажмите **"+ New"**
2. Выберите **"Database"** → **"Add PostgreSQL"**
3. Railway автоматически создаст базу и добавит переменную `DATABASE_URL`

### Шаг 3: Настройте переменные окружения

В настройках сервиса (Settings → Variables) добавьте:

```
CORS_ORIGINS=["https://web.telegram.org","http://localhost:3000"]
TELEGRAM_BOT_TOKEN=ваш_токен_бота (опционально)
TELEGRAM_SECRET_KEY=ваш_секретный_ключ (опционально)
```

**Важно:** Railway автоматически добавит свой домен в CORS через переменную `RAILWAY_PUBLIC_DOMAIN`

### Шаг 4: Настройте деплой

1. В настройках сервиса (Settings → Deploy) укажите:
   - **Root Directory**: `backend`
   - **Start Command**: `alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port $PORT`

2. Railway автоматически:
   - Установит зависимости из `requirements.txt`
   - Применит миграции Alembic
   - Запустит сервер

### Шаг 5: Получите URL

1. После деплоя Railway предоставит публичный URL вида: `https://ваш-проект.up.railway.app`
2. Скопируйте этот URL — это будет ваш backend URL

## Деплой Frontend

### Вариант 1: Vercel (рекомендуется для frontend)

1. Перейдите на [vercel.com](https://vercel.com)
2. Подключите GitHub репозиторий
3. Настройки:
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Environment Variables**:
     - `VITE_API_URL`: ваш Railway backend URL (например: `https://ваш-проект.up.railway.app`)

### Вариант 2: Railway (тоже можно)

1. В том же проекте Railway добавьте новый сервис
2. Выберите **"Deploy from GitHub repo"** → ваш репозиторий
3. Настройки:
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Start Command**: `npx serve -s dist -l $PORT`
   - **Environment Variables**:
     - `VITE_API_URL`: ваш Railway backend URL

## Обновление кнопки в BotFather

После получения URL frontend:

1. Откройте @BotFather
2. `/setmenubutton` → ваш бот → Web App
3. Вставьте ваш frontend URL (от Vercel или Railway)

## Проверка работы

1. Откройте Mini App в Telegram
2. Попробуйте создать товар
3. Проверьте, что данные сохраняются

## Обновление кода

После каждого push в GitHub:
- Railway автоматически передеплоит backend
- Vercel автоматически передеплоит frontend

## Важные замечания

- Railway предоставляет бесплатный план с $5 кредитами в месяц
- После 30 дней неактивности проект может быть приостановлен
- Для продакшена рекомендуется настроить кастомный домен
- Все переменные окружения настраиваются в Railway Dashboard

