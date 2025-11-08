/**
 * Точка входа в приложение
 */
import { initTelegramWebApp } from './utils/telegram';
import { apiClient } from './services/api';
import { renderProductList } from './components/ProductList';
import { renderProductForm } from './components/ProductForm';

// Инициализация Telegram WebApp
const tg = initTelegramWebApp();

// Состояние приложения
let currentState = 'list'; // 'list' | 'form' | 'edit'
let currentEditId = null;
let products = [];

// Инициализация приложения
async function init() {
    console.log('ReStocker Mini App loaded');
    
    // Устанавливаем тему Telegram, если доступна
    if (tg) {
        document.documentElement.style.setProperty('--tg-theme-bg-color', tg.themeParams.bg_color || '#ffffff');
        document.documentElement.style.setProperty('--tg-theme-text-color', tg.themeParams.text_color || '#000000');
        document.documentElement.style.setProperty('--tg-theme-button-color', tg.themeParams.button_color || '#2481cc');
        document.documentElement.style.setProperty('--tg-theme-button-text-color', tg.themeParams.button_text_color || '#ffffff');
    }
    
    await loadProducts();
    render();
}

// Загрузка товаров
async function loadProducts() {
    try {
        products = await apiClient.getProducts();
        console.log('Products loaded:', products);
        // Убираем сообщение об ошибке, если оно было
        const errorDiv = document.getElementById('error-message');
        if (errorDiv) {
            errorDiv.remove();
        }
    } catch (error) {
        console.error('Failed to load products:', error);
        // Не показываем ошибку, если это просто пустой список (новый пользователь)
        // Показываем только если это реальная ошибка подключения
        if (error.message && !error.message.includes('Failed to fetch') && !error.message.includes('load failed')) {
            const errorMsg = `Не удалось загрузить товары: ${error.message}`;
            showError(errorMsg);
            showErrorOnScreen(errorMsg);
        }
        products = [];
    }
}

// Отображение интерфейса
function render() {
    const app = document.getElementById('app');
    
    if (currentState === 'form' || currentState === 'edit') {
        const product = currentState === 'edit' && currentEditId 
            ? products.find(p => p.id === currentEditId) 
            : null;
        app.innerHTML = renderProductForm(product);
        setupFormHandlers();
    } else {
        app.innerHTML = renderProductList(products, addProduct, editProduct, deleteProduct);
    }
}

// Обработчики действий
window.addProduct = function() {
    currentState = 'form';
    currentEditId = null;
    render();
};

window.editProduct = function(id) {
    currentState = 'edit';
    currentEditId = id;
    render();
};

window.deleteProduct = async function(id) {
    if (!confirm('Вы уверены, что хотите удалить этот товар?')) {
        return;
    }
    
    try {
        await apiClient.deleteProduct(id);
        await loadProducts();
        render();
        showSuccess('Товар удален');
    } catch (error) {
        console.error('Failed to delete product:', error);
        showError('Не удалось удалить товар: ' + error.message);
    }
};

window.closeForm = function() {
    currentState = 'list';
    currentEditId = null;
    render();
};

// Настройка обработчиков формы
function setupFormHandlers() {
    const form = document.getElementById('productForm');
    if (!form) return;
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        const productData = {
            name: formData.get('name'),
            category: formData.get('category') || null,
            unit: formData.get('unit'),
            quantity: parseFloat(formData.get('quantity')),
            threshold: parseFloat(formData.get('threshold')) || 0,
        };
        
        try {
            // Валидация данных перед отправкой
            if (!productData.name || !productData.name.trim()) {
                showError('Название товара обязательно для заполнения');
                return;
            }
            
            if (!productData.unit || !productData.unit.trim()) {
                showError('Единица измерения обязательна для заполнения');
                return;
            }
            
            if (isNaN(productData.quantity)) {
                showError('Текущий остаток должен быть числом');
                return;
            }
            
            if (currentState === 'edit' && currentEditId) {
                await apiClient.updateProduct(currentEditId, productData);
                showSuccess('Товар обновлен');
            } else {
                await apiClient.createProduct(productData);
                showSuccess('Товар создан');
            }
            
            await loadProducts();
            currentState = 'list';
            currentEditId = null;
            render();
        } catch (error) {
            console.error('Failed to save product:', error);
            
            // Улучшенные сообщения об ошибках
            let errorMessage = 'Не удалось сохранить товар';
            
            if (error.message.includes('already exists') || error.message.includes('уже существует')) {
                errorMessage = 'Товар с таким названием уже существует';
            } else if (error.message.includes('Failed to fetch') || error.message.includes('load failed')) {
                errorMessage = 'Не удалось подключиться к серверу. Проверьте, что backend туннель запущен';
            } else if (error.message) {
                errorMessage = `Не удалось сохранить товар: ${error.message}`;
            }
            
            showError(errorMessage);
        }
    });
}

// Уведомления
function showError(message) {
    if (tg?.showAlert) {
        tg.showAlert(message);
    } else {
        alert('Ошибка: ' + message);
    }
}

function showErrorOnScreen(message) {
    const app = document.getElementById('app');
    if (app) {
        let errorDiv = document.getElementById('error-message');
        if (!errorDiv) {
            errorDiv = document.createElement('div');
            errorDiv.id = 'error-message';
            app.insertBefore(errorDiv, app.firstChild);
        }
        errorDiv.style.cssText = 'padding: 15px; background: #ffebee; color: #c62828; border-radius: 8px; margin: 10px;';
        errorDiv.innerHTML = `<strong>Ошибка:</strong> ${message}`;
    }
}

function showSuccess(message) {
    if (tg?.showAlert) {
        tg.showAlert(message);
    } else {
        alert(message);
    }
}

// Запуск приложения
init();
