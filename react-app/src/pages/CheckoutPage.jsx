import React, { useEffect, useState } from "react";
import CartItem from "../components/CartItems";
import CheckoutForm from "../components/CheckoutForm";

function CheckoutPage() {
    const [cart, setCart] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch cart items from the backend
    useEffect(() => {
        fetch("http://localhost:5000/api/cart", {
            method: "GET",
            credentials: "include", // Ensures session cookies are sent
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Failed to fetch cart items");
                }
                return response.json();
            })
            .then((data) => {
                setCart(data.cart); // Set the cart items from the response
                setLoading(false);
            })
            .catch((err) => {
                setError(err.message);
                setLoading(false);
            });
    }, []);

    // Render loading state
    if (loading) {
        return <div>Loading your cart...</div>;
    }

    // Render error state
    if (error) {
        return <div>Error: {error}</div>;
    }

    // Render empty cart state
    if (cart.length === 0) {
        return <div>Your cart is empty. Add items to proceed to checkout.</div>;
    }

    // Render checkout page with cart items
    return (
        <div className="cart-page">
            <h1>Your Shopping Cart</h1>
            <div className="cart-items">
                {cart.map((item) => (
                    <div key={item.product_id} className="cart-item">
                        <img
                            src={item.image_url}
                            alt={item.description}
                            width="100"
                        />
                        <div className="cart-item-details">
                            <h2>{item.description}</h2>
                            <p>Color: {item.color}</p>
                            <p>Size: {item.size}</p>
                            <p>Quantity: {item.quantity}</p>
                        </div>
                    </div>
                ))}
            </div>

            <CheckoutForm />
        </div>
    );
}

export default CheckoutPage;
