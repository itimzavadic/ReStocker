/**
 * Утилиты для работы с Telegram WebApp
 */

export function initTelegramWebApp() {
    if (window.Telegram?.WebApp) {
        const tg = window.Telegram.WebApp;
        tg.ready();
        tg.expand();
        return tg;
    }
    // Fallback для разработки вне Telegram
    console.warn('Telegram WebApp not available');
    return null;
}

export function getTelegramUser() {
    if (window.Telegram?.WebApp?.initDataUnsafe?.user) {
        return window.Telegram.WebApp.initDataUnsafe.user;
    }
    return null;
}

