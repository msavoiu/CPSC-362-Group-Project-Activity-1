import React from "react";

function CheckoutForm() {
    const [state, setState] = React.useState({
        name: "",
        address: "",
        cardNumber: ""
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setState({
            ...state,
            [name]: value
        });
    };

    const onSubmit = (e) => {
        e.preventDefault();
        console.log("Processing payment for:", state);
        // Add API logic here
    };

    return (
        <form onSubmit={onSubmit} className="checkout-form">
            <h1>Checkout</h1>
            <input
                type="text"
                name="name"
                placeholder="Full Name"
                value={state.name}
                onChange={handleChange}
            />
            <input
                type="text"
                name="address"
                placeholder="Shipping Address"
                value={state.address}
                onChange={handleChange}
            />
            <input
                type="text"
                name="cardNumber"
                placeholder="Card Number"
                value={state.cardNumber}
                onChange={handleChange}
            />
            <button type="submit">Place Order</button>
        </form>
    );
}

export default CheckoutForm;
