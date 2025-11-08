# Быстрый деплой ReStocker на Railway

## Шаг 1: Подготовка GitHub репозитория

```bash
# В корне проекта
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/ваш-username/restocker.git
git push -u origin main
```

## Шаг 2: Деплой Backend на Railway

1. Перейдите на [railway.app](https://railway.app) и войдите через GitHub
2. Нажмите **"New Project"** → **"Deploy from GitHub repo"**
3. Выберите ваш репозиторий
4. Railway автоматически определит Python проект

### Добавьте PostgreSQL:

1. В проекте нажмите **"+ New"** → **"Database"** → **"Add PostgreSQL"**
2. Railway автоматически добавит переменную `DATABASE_URL`

### Настройте деплой:

1. В настройках сервиса (Settings):
   - **Root Directory**: `backend`
   - Railway автоматически применит миграции (через `release` в Procfile)

2. После деплоя скопируйте **публичный URL** (например: `https://restocker-backend.up.railway.app`)

## Шаг 3: Деплой Frontend на Vercel

1. Перейдите на [vercel.com](https://vercel.com) и войдите через GitHub
2. Нажмите **"Add New Project"**
3. Выберите ваш репозиторий
4. Настройки:
   - **Root Directory**: `frontend`
   - **Framework Preset**: Vite
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Environment Variables**:
     - `VITE_API_URL`: ваш Railway backend URL (например: `https://restocker-backend.up.railway.app`)

5. Нажмите **"Deploy"**
6. После деплоя скопируйте **публичный URL** (например: `https://restocker-frontend.vercel.app`)

## Шаг 4: Обновите кнопку в BotFather

1. Откройте @BotFather
2. `/setmenubutton` → ваш бот → Web App
3. Вставьте ваш Vercel frontend URL

## Готово! 🎉

Теперь ваше приложение работает на стабильных URL без туннелей!

## Обновление кода

После каждого `git push`:
- Railway автоматически передеплоит backend
- Vercel автоматически передеплоит frontend

