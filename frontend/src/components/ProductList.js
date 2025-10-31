/**
 * Компонент списка товаров
 */
export function ProductList({ products, onAdd, onWithdraw }) {
    const listItems = products.map(product => `
        <div class="product-item ${product.quantity < product.threshold ? 'low-stock' : ''}">
            <div class="product-name">${product.name}</div>
            <div class="product-quantity">Остаток: ${product.quantity} ${product.unit}</div>
            <div class="product-threshold">Порог: ${product.threshold} ${product.unit}</div>
            <button onclick="onWithdraw(${product.id})">Списать</button>
        </div>
    `).join('');

    return `
        <div class="product-list">
            <div class="header">
                <h2>Склад</h2>
                <button onclick="onAdd()">+ Добавить товар</button>
            </div>
            ${listItems}
        </div>
    `;
}

