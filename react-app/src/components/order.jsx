import React from "react";

function Order() {
    // Fetch order information using its ID # from props

    const products = [];
    const productsList = [];

    for (const product of products) {
        productsList.push(<li>product.name</li>);
    }

    return (
        <>
            <h1>Order #</h1>
            <p>Placed: XX/XX/XXXX</p>

        </>
    );
}

export default Order;
