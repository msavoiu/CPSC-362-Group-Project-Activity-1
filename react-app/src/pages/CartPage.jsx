import React from "react";
import CartItem from "../components/CartItems";

function CartPage() {
    // Mock cart items — replace with real data from backend or context
    const cart = [
        //no cart as of now mock item is vital hoodie
        //{ id: 1, name: "Vital Hoodie", quantity: 1, price: 59.99, image: "/img/hoodie.jpg" }
    ];

    return (
        <div className="cart-page">
            <h1>Your Cart</h1>
            {cart.length > 0 ? (
                <>
                    {cart.map(item => (
                        <CartItem key={item.id} item={item} />
                    ))}
                    <button onClick={() => window.location.href = "/checkout"}>
                        Proceed to Checkout
                    </button>
                </>
            ) : (
                <p>Your cart is empty.</p>
            )}
        </div>
    );
}

export default CartPage;
