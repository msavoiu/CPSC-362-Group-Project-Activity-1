import React from "react";
import CatalogProduct from "../components/CatalogProduct";

function CatalogPage() {
    const products = [
        { id: 1, name: "Vital Hoodie", price: 59.99, image: "/hoodie.png" },
        { id: 2, name: "Vital Tee", price: 29.99, image: "/shirt.png" },
    ];

    return (
        <div className="catalog-page">
            <h1>Shop All</h1>
            <div className="product-list">
                {products.map((product) => (
                    <CatalogProduct key={product.id} product={product} />
                ))}
            </div>
        </div>
    );
}

export default CatalogPage;
