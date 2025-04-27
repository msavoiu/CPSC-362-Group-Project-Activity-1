import React from "react";
import { useParams } from "react-router-dom";

function ProductPage() {
    const { id } = useParams();

    // Example static product data
    const product = {
        id,
        name: "Vital Hoodie",
        description: "A comfy, premium hoodie for everyday wear.",
        price: 59.99,
        image: process.env.PUBLIC_URL + "/img/hoodie.jpg" // Access from /public/img/
    };

    const handleAddToCart = () => {
        // Placeholder function - connect this to backend or global state later
        console.log("Add to cart clicked:", product);
    };

    return (
        <div className="product-page">
            <img src={product.image} alt={product.name} width="300" />
            <h1>{product.name}</h1>
            <p>{product.description}</p>
            <p>${product.price.toFixed(2)}</p>
            <button onClick={handleAddToCart}>Add to Cart</button>
        </div>
    );
}

export default ProductPage;
