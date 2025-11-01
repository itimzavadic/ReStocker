/**
 * Компонент списка товаров
 */
export function renderProductList(products, onAdd, onEdit, onDelete) {
    if (!products || products.length === 0) {
        return `
            <div class="product-list">
                <div class="header">
                    <h2>Склад</h2>
                    <button class="btn-primary" onclick="window.addProduct()">+ Добавить товар</button>
                </div>
                <div class="empty-state">
                    <p>У вас пока нет товаров</p>
                    <button class="btn-primary" onclick="window.addProduct()">Добавить первый товар</button>
                </div>
            </div>
        `;
    }

    const listItems = products.map(product => {
        const isLowStock = product.quantity <= product.threshold;
        const stockClass = isLowStock ? 'low-stock' : '';
        
        return `
            <div class="product-item ${stockClass}" data-product-id="${product.id}">
                <div class="product-info">
                    <div class="product-name">${escapeHtml(product.name)}</div>
                    <div class="product-details">
                        <span class="product-category">${escapeHtml(product.category || 'Без категории')}</span>
                        <span class="product-unit">${escapeHtml(product.unit)}</span>
                    </div>
                    <div class="product-stock">
                        <span class="stock-label">Остаток:</span>
                        <span class="stock-quantity ${isLowStock ? 'warning' : ''}">${product.quantity}</span>
                        ${product.threshold > 0 ? `<span class="stock-threshold">Порог: ${product.threshold}</span>` : ''}
                    </div>
                </div>
                <div class="product-actions">
                    <button class="btn-small" onclick="window.editProduct(${product.id})">✏️</button>
                    <button class="btn-small btn-danger" onclick="window.deleteProduct(${product.id})">🗑️</button>
                </div>
            </div>
        `;
    }).join('');

    return `
        <div class="product-list">
            <div class="header">
                <h2>Склад (${products.length})</h2>
                <button class="btn-primary" onclick="window.addProduct()">+ Добавить товар</button>
            </div>
            <div class="product-items">
                ${listItems}
            </div>
        </div>
    `;
}

function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
