import React from "react";
import CatalogProduct from "../components/CatalogProduct";

function CatalogPage() {
    // Mock data — your backend team should replace this with API fetch
    const products = [
        { id: 1, name: "Vital Hoodie", price: 59.99, image: "/img/hoodie.jpg" },
        { id: 2, name: "Vital Tee", price: 29.99, image: "/img/tee.jpg" },
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
