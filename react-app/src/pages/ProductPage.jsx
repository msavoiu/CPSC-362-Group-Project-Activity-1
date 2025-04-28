import React from "react";
import { useParams } from "react-router-dom";
import { useCart } from "../context/CartContext.jsx"; // Make sure path is correct

function ProductPage() {
    const { id } = useParams();
    const { addToCart } = useCart();

    let product;

    if (id == 1) {
        product = {
            id,
            name: "Vital Hoodie",
            description: "A comfy, premium hoodie for everyday wear.",
            price: 59.99,
            image: "/hoodie.png"
        };
    } else {
        product = {
            id,
            name: "Vital Tee",
            description: "A breathable, basic t-shirt. Perfect for layering.",
            price: 29.99,
            image: "/shirt.png"
        }; 
    }

    const handleAddToCart = async () => {
        fetch('http://localhost:5000/api/cart/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include', // Ensures cookies (like session cookies) are sent with the request
            body: JSON.stringify({
                product_id: id,
                quantity: 1
            }),
        })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    console.log(data.message); // Handle success or error message
                }
                alert("Added to cart!")
            })
            .catch(error => {
                console.error('Error:', error); // Handle any network or other errors
            });
    };

    return (
        <div className="product-page">
            <img src={product.image} alt={product.name} width="300" />
            <h1>{product.name}</h1>
            <p>{product.description}</p>
            <p>${product.price.toFixed(2)}</p>
            <button
                className="button"
                onClick={handleAddToCart}>Add to Cart</button>
        </div>
    );
}

export default ProductPage;