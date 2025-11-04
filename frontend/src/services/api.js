/**
 * API клиент для взаимодействия с backend
 */
// В режиме разработки используем относительные пути (через Vite proxy)
// В продакшене можно указать VITE_API_URL в .env
// Если мы в Telegram Mini App через туннель, используем абсолютный URL backend
let API_BASE_URL = import.meta.env.VITE_API_URL || '';

// Если находимся на домене localhost.run или в Telegram WebApp - используем туннель backend
if (!API_BASE_URL && (window.location.hostname.includes('lhr.life') || window.Telegram?.WebApp)) {
    // URL backend туннеля (обновите при изменении туннеля)
    API_BASE_URL = 'https://fcc85d962b95bc.lhr.life';
    console.log('Detected tunnel domain or Telegram WebApp, using backend tunnel:', API_BASE_URL);
} else {
    console.log('Using relative paths or VITE_API_URL:', API_BASE_URL || '(relative via Vite proxy)');
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
        
        console.log('API Request:', {
            url,
            endpoint,
            baseURL: this.baseURL,
            telegramId,
            method: options.method || 'GET'
        });
        
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
            console.log('Fetching:', url, config);
            const response = await fetch(url, config);
            
            console.log('Response status:', response.status, response.statusText);
            
            if (!response.ok) {
                const errorText = await response.text();
                let errorData;
                try {
                    errorData = JSON.parse(errorText);
                } catch {
                    errorData = { detail: errorText || `HTTP ${response.status}` };
                }
                console.error('API Error:', errorData, 'Response text:', errorText);
                throw new Error(errorData.detail || errorData.message || `API error: ${response.status}`);
            }

            // Для DELETE запросов может не быть body
            if (response.status === 204) {
                return null;
            }

            const data = await response.json();
            console.log('API Success:', data);
            return data;
        } catch (error) {
            console.error('API request failed:', error);
            console.error('Error details:', {
                message: error.message,
                url,
                baseURL: this.baseURL,
                stack: error.stack
            });
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
