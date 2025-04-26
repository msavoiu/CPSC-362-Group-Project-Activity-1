import { useState } from "react"
import "./App.css"
import { Routes, Route } from "react-router-dom";

// Page components
import Login from "./pages/login.jsx";
import Register from "./pages/register.jsx";
import Navbar from "./components/navbar.jsx"

import Homepage from "./pages/Homepage.jsx";
import CheckoutPage from "./pages/CheckoutPage.jsx";
import CatalogPage from "./pages/CatalogPage.jsx";
import ProductPage from "./pages/ProductPage.jsx";
import CartPage from "./pages/CartPage.jsx";

function App() {
    const [count, setCount] = useState(0)
    return (
        <>
            <Navbar />
            <Routes>
                { <Route path="/register" element={<Register />} /> }
                <Route path="/login" element={<Login />} />
                <Route path="/home" element={<Homepage />} />
                <Route path="/checkout" element={<CheckoutPage />} />
                <Route path="/catalog" element={<CatalogPage />} />
                <Route path="/product/:id" element={<ProductPage />} /> 
                <Route path="/cart" element={<CartPage />} />
                {/* <Route path="/register" element={<Register />} />
                <Route path="/products" element={<Catalog />} />
                <Route path="/about" element={<About />} /> */}
            </Routes>
        </>
    );
}

export default App;
