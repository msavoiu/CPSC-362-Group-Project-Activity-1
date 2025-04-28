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

    const onSubmit = async (e) => {
        e.preventDefault();
    
        try {
            const response = await fetch("http://localhost:5000/api/checkout", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                credentials: "include", // Ensures session cookies are sent
            });
    
            if (response.ok) {
                const data = await response.json();
                alert(data.message); // Display success message
                console.log("Order placed successfully:", data.message);
                window.location.href = "/profile";
            } else {
                const errorData = await response.json();
                alert(`Error: ${errorData.message}`); // Display error message
                console.error("Error placing order:", errorData.message);
            }
        } catch (error) {
            console.error("Network error:", error);
            alert("An error occurred while placing the order. Please try again.");
        }
    };

    return (
        <div className="form-div">
            <form onSubmit={onSubmit} className="form">
                <h1>Checkout</h1>
                <input
                    type="text"
                    name="name"
                    placeholder="Full Name"
                    value={state.name}
                    onChange={handleChange}
                />
                <input
                    type="textarea"
                    name="address"
                    placeholder="Shipping Address"
                    value={state.address}
                    onChange={handleChange}
                />
                <input
                    type="password"
                    name="cardNumber"
                    placeholder="Card Number"
                    value={state.cardNumber}
                    onChange={handleChange}
                />
                <button className="button" onSubmit={onSubmit}>Place Order</button>
            </form>
        </div>
    );
}

export default CheckoutForm;
