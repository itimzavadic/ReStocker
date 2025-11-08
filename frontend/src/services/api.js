/**
 * API клиент для взаимодействия с backend
 */
// В режиме разработки используем относительные пути (через Vite proxy)
// В продакшене можно указать VITE_API_URL в .env
// Если мы в Telegram Mini App через туннель, используем абсолютный URL backend
let API_BASE_URL = import.meta.env.VITE_API_URL || '';

// Если VITE_API_URL не установлен и мы в Telegram WebApp или на домене туннеля - используем туннель backend
// Для продакшена (Railway/Vercel) VITE_API_URL должен быть установлен через переменные окружения
if (!API_BASE_URL && (window.location.hostname.includes('lhr.life') || window.Telegram?.WebApp)) {
    // URL backend туннеля для локальной разработки (обновите при изменении туннеля)
    // ВАЖНО: Обновите этот URL после каждого перезапуска backend туннеля!
    API_BASE_URL = 'https://8ea1cb17ced530.lhr.life';
}

class ApiClient {
    constructor(baseURL) {
        this.baseURL = baseURL;
    }
    
    // Экспортируем метод для получения telegram_id для отладки
    getTelegramId() {
        return this._getTelegramId();
    }
    
    /**
     * Получить telegram_id из Telegram WebApp или из localStorage (для разработки)
     */
    _getTelegramId() {
        // Пробуем получить из Telegram WebApp
        if (window.Telegram?.WebApp?.initDataUnsafe?.user?.id) {
            return window.Telegram.WebApp.initDataUnsafe.user.id;
        }
        // Для разработки - используем localStorage
        const devId = localStorage.getItem('dev_telegram_id');
        if (devId) {
            return parseInt(devId);
        }
        // Если нет, создаем временный ID для разработки
        const newId = Date.now();
        localStorage.setItem('dev_telegram_id', newId.toString());
        return newId;
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const telegramId = this._getTelegramId();
        
        const config = {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                'X-Telegram-Id': telegramId.toString(),
                ...options.headers,
            },
        };

        // Добавляем body, если есть
        if (options.body) {
            config.body = typeof options.body === 'string' 
                ? options.body 
                : JSON.stringify(options.body);
        }

        try {
            const response = await fetch(url, config);
            
            if (!response.ok) {
                const errorText = await response.text();
                let errorData;
                try {
                    errorData = JSON.parse(errorText);
                } catch {
                    errorData = { detail: errorText || `HTTP ${response.status}` };
                }
                throw new Error(errorData.detail || errorData.message || `API error: ${response.status}`);
            }

            // Для DELETE запросов может не быть body
            if (response.status === 204) {
                return null;
            }

            const data = await response.json();
            return data;
        } catch (error) {
            // Улучшаем сообщение об ошибке для пользователя
            if (error.message.includes('Failed to fetch') || error.message.includes('NetworkError') || error.name === 'TypeError') {
                throw new Error('Не удалось подключиться к серверу');
            }
            throw error;
        }
    }

    // Products
    async getProducts() {
        return this.request('/api/v1/products');
    }

    async getProduct(productId) {
        return this.request(`/api/v1/products/${productId}`);
    }

    async createProduct(productData) {
        return this.request('/api/v1/products', {
            method: 'POST',
            body: productData,
        });
    }

    async updateProduct(productId, productData) {
        return this.request(`/api/v1/products/${productId}`, {
            method: 'PUT',
            body: productData,
        });
    }

    async deleteProduct(productId) {
        return this.request(`/api/v1/products/${productId}`, {
            method: 'DELETE',
        });
    }

    // Buttons
    async getButtons() {
        return this.request('/api/v1/buttons');
    }

    async createButton(buttonData) {
        return this.request('/api/v1/buttons', {
            method: 'POST',
            body: buttonData,
        });
    }

    async executeButton(buttonId) {
        return this.request(`/api/v1/buttons/${buttonId}/execute`, {
            method: 'POST',
        });
    }
}

export const apiClient = new ApiClient(API_BASE_URL);
