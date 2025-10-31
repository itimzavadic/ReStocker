/**
 * Первый экран - выбор режима использования
 */
export function WelcomePage({ onSelectMode }) {
    return `
        <div class="welcome-page">
            <h1>Добро пожаловать в ReStocker</h1>
            <p>Вы используете CRM?</p>
            <div class="buttons">
                <button onclick="onSelectMode('crm')">Да, использую CRM</button>
                <button onclick="onSelectMode('manual')">Нет, ручной режим</button>
            </div>
        </div>
    `;
}

