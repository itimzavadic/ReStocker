# Быстрый старт ReStocker

## Запуск для тестирования в Telegram Mini App

### 1. Запуск Backend

```bash
cd backend

# Создать виртуальное окружение (если еще не создано)
python3 -m venv venv
source venv/bin/activate  # на Windows: venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt

# Настроить .env файл (скопировать из .env.example)
cp .env.example .env
# Отредактировать .env и указать свои настройки БД

# Применить миграции (если БД еще не создана)
alembic upgrade head

# Запустить сервер
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend будет доступен по адресу: `http://localhost:8000`

### 2. Запуск Frontend

```bash
cd frontend

# Установить зависимости
npm install

# Запустить dev сервер
npm run dev
```

Frontend будет доступен по адресу: `http://localhost:3000`

### 3. Настройка Telegram Bot для Mini App

1. Создайте бота через @BotFather в Telegram
2. Получите токен бота
3. Настройте команду `/setmenubutton` или создайте inline keyboard с кнопкой для Mini App
4. В настройках бота укажите URL вашего Mini App:
   ```
   https://ваш-домен.com или для теста: https://ваш-ngrok-url.ngrok.io
   ```

### 4. Для локальной разработки (без Telegram)

Если вы тестируете локально без Telegram:

1. Откройте `http://localhost:3000` в браузере
2. Приложение автоматически создаст временный `telegram_id` в localStorage
3. Все API запросы будут использовать этот ID

### 5. Для тестирования в Telegram Mini App

#### Вариант 1: Использовать ngrok для туннеля

```bash
# Установите ngrok если еще не установлен
# https://ngrok.com/download

# Создать туннель для frontend
ngrok http 3000

# Получите HTTPS URL (например: https://abc123.ngrok.io)
# Этот URL нужно указать в настройках Telegram Bot
```

#### Вариант 2: Использовать ngrok для backend (если frontend на другом домене)

```bash
# Туннель для backend
ngrok http 8000

# В frontend/.env или vite.config.js укажите:
# VITE_API_URL=https://ваш-ngrok-url.ngrok.io
```

### 6. Важные замечания

- Backend должен быть доступен по HTTPS для работы Telegram WebApp
- Используйте ngrok или другой туннель для локальной разработки
- В продакшене используйте реальный домен с SSL сертификатом

### Тестирование API

После запуска backend, вы можете протестировать API:

```bash
# Получить список товаров (нужен заголовок X-Telegram-Id)
curl -H "X-Telegram-Id: 123456789" http://localhost:8000/api/v1/products/

# Создать товар
curl -X POST http://localhost:8000/api/v1/products/ \
  -H "Content-Type: application/json" \
  -H "X-Telegram-Id: 123456789" \
  -d '{"name": "Пакет упаковочный", "unit": "шт", "quantity": 10, "threshold": 5}'
```

### Проверка работы

1. ✅ Backend запущен и отвечает на `/health`
2. ✅ Frontend запущен и открывается в браузере
3. ✅ Можно создавать и редактировать товары
4. ✅ Данные сохраняются в БД

Если что-то не работает:
- Проверьте логи backend в консоли
- Откройте DevTools в браузере и проверьте Console на ошибки
- Убедитесь, что БД настроена правильно
- Проверьте, что миграции применены: `alembic current`

