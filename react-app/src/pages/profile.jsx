import React from "react";
import Order from "./../components/order.jsx";

function ProfilePage() {
    const orders = []; // Fetch request to get all the orders corresponding to the user
    const ordersList = [];

    for (const order of orders) {
        ordersList.push(<Order />); // Pass order ID in as a prop?
    }

    return (
        <>
            <div className="profile-block">
                <img src="./../static/usericon.png" alt="User icon"></img>
                <h1>Firstname Lastname</h1>
                <h3>user@email.com</h3>
            </div>

            <h2>Recent Orders</h2>
            <ul>
                {orders}
            </ul>
        </>
    );
}

export default ProfilePage;
