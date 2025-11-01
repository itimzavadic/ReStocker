/**
 * API клиент для взаимодействия с backend
 */
// В режиме разработки используем относительные пути (через Vite proxy)
// В продакшене можно указать VITE_API_URL в .env
const API_BASE_URL = import.meta.env.VITE_API_URL || '';

class ApiClient {
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    /**
     * Получить telegram_id из Telegram WebApp или из localStorage (для разработки)
     */
    getTelegramId() {
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
        const telegramId = this.getTelegramId();
        
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
                const errorData = await response.json().catch(() => ({ detail: 'Unknown error' }));
                throw new Error(errorData.detail || `API error: ${response.status}`);
            }

            // Для DELETE запросов может не быть body
            if (response.status === 204) {
                return null;
            }

            return await response.json();
        } catch (error) {
            console.error('API request failed:', error);
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
