import React from "react";

function CartItem({ item }) {
    return (
        <div className="cart-item">
            <img src={item.image} alt={item.name} width="100" />
            <div>
                <h3>{item.name}</h3>
                <p>Quantity: {item.quantity}</p>
                <p>Price: ${item.price.toFixed(2)}</p>
            </div>
        </div>
    );
}

export default CartItem;
