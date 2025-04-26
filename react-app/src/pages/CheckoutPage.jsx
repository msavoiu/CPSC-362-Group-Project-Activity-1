import React from "react";
import CartItem from "../components/CartItems";
import CheckoutForm from "../components/CheckoutForm";

function CheckoutPage() {
    // Your backend team should replace this with real cart data
    const cart = [
        //cart items}
    ];

    return (
        <div className="checkout-page">
            <h1>Checkout</h1>
            <div className="checkout-cart-items">
                {cart.map(item => (
                    <CartItem key={item.id} item={item} />
                ))}
            </div>
            <CheckoutForm />
        </div>
    );
}

export default CheckoutPage;
