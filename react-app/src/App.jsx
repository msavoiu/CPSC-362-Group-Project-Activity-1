import "./App.css"
import { Routes, Route } from "react-router-dom";

// Page components
import Login from "./pages/login.jsx";
import Register from "./pages/register.jsx";
import Navbar from "./components/navbar.jsx";
import Profile from "./pages/profile.jsx";

import Homepage from "./pages/Homepage.jsx";
import CheckoutPage from "./pages/CheckoutPage.jsx";
import CatalogPage from "./pages/CatalogPage.jsx";
import ProductPage from "./pages/ProductPage.jsx";
import CartPage from "./pages/CartPage.jsx";
import { CartProvider } from './context/CartContext.jsx';

function App() {
    return (
        <>
            <CartProvider>
                <Navbar />
                <div className="page-content">
                    <Routes>
                        <Route path="/" element={<Homepage />} />
                        <Route path="/register" element={<Register />} />
                        <Route path="/login" element={<Login />}/>
                        <Route path="/profile" element={<Profile />}/>
                        <Route path="/checkout" element={<CheckoutPage />} />
                        <Route path="/catalog" element={<CatalogPage />} />
                        <Route path="/product/:id" element={<ProductPage />} /> 
                        <Route path="/cart" element={<CartPage />} />
                        <Route path="/register" element={<Register />} />
                        {/* <Route path="/about" element={<About />} /> */}
                    </Routes>
                </div>
            </CartProvider>
        </>
    );
}

export default App;
