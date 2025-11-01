/**
 * Форма для создания/редактирования товара
 */
export function renderProductForm(product = null) {
    const isEdit = !!product;
    const title = isEdit ? 'Редактировать товар' : 'Добавить товар';
    
    return `
        <div class="product-form-container">
            <div class="form-header">
                <h2>${title}</h2>
                <button class="btn-close" onclick="window.closeForm()">✕</button>
            </div>
            <form id="productForm" class="product-form">
                <div class="form-group">
                    <label for="name">Название товара *</label>
                    <input type="text" id="name" name="name" required 
                           value="${product ? escapeHtml(product.name) : ''}" 
                           placeholder="Например: Пакет упаковочный">
                </div>
                
                <div class="form-group">
                    <label for="category">Категория</label>
                    <input type="text" id="category" name="category" 
                           value="${product ? escapeHtml(product.category || '') : ''}" 
                           placeholder="Например: Упаковка">
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label for="unit">Единица измерения *</label>
                        <input type="text" id="unit" name="unit" required 
                               value="${product ? escapeHtml(product.unit) : 'шт'}" 
                               placeholder="шт, кг, л">
                    </div>
                    
                    <div class="form-group">
                        <label for="quantity">Текущий остаток *</label>
                        <input type="number" id="quantity" name="quantity" step="0.01" required 
                               value="${product ? product.quantity : '0'}" 
                               min="0">
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="threshold">Порог оповещения</label>
                    <input type="number" id="threshold" name="threshold" step="0.01" 
                           value="${product ? product.threshold : '0'}" 
                           min="0" 
                           placeholder="При достижении этого уровня будет уведомление">
                    <small>Оставьте 0, если не нужно уведомление</small>
                </div>
                
                <div class="form-actions">
                    <button type="button" class="btn-secondary" onclick="window.closeForm()">Отмена</button>
                    <button type="submit" class="btn-primary">${isEdit ? 'Сохранить' : 'Создать'}</button>
                </div>
            </form>
        </div>
    `;
}

function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

