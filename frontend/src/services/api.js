/**
 * API клиент для взаимодействия с backend
 */
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

class ApiClient {
    constructor(baseURL) {
        this.baseURL = baseURL;
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const config = {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
        };

        const response = await fetch(url, config);
        
        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }

        return response.json();
    }

    // Products
    async getProducts() {
        return this.request('/api/v1/products');
    }

    async createProduct(productData) {
        return this.request('/api/v1/products', {
            method: 'POST',
            body: JSON.stringify(productData),
        });
    }

    // Buttons
    async getButtons() {
        return this.request('/api/v1/buttons');
    }

    async createButton(buttonData) {
        return this.request('/api/v1/buttons', {
            method: 'POST',
            body: JSON.stringify(buttonData),
        });
    }

    async executeButton(buttonId) {
        return this.request(`/api/v1/buttons/${buttonId}/execute`, {
            method: 'POST',
        });
    }
}

export const apiClient = new ApiClient(API_BASE_URL);

