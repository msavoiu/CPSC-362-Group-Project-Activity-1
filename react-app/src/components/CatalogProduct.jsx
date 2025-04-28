import React from "react";

function CatalogProduct({ product }) {
    return (
        <div className="product-card">
            <img src={product.image} alt={product.name} width="200" />
            <h2>{product.name}</h2>
            <p>${product.price.toFixed(2)}</p>
            <button
                onClick={() => window.location.href = `/product/${product.id}`}
                className="button">
                View Product
            </button>
        </div>
    );
}

export default CatalogProduct;
