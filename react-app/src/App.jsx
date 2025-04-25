import { useState } from "react"
import "./App.css"
import { Routes, Route } from "react-router-dom";

// Page components
import Login from "./pages/login.jsx";
import Register from "./pages/register.jsx";
import Navbar from "./components/navbar.jsx";
import Profile from "./pages/profile.jsx";

function App() {
    return (
        <>
            <Navbar />
            <Routes>
                {/* <Route path="/" element={<Home />} /> */}
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/profile" element={<Profile />}/>
                {/* <Route path="/products" element={<Catalog />} /> */}
                {/* <Route path="/about" element={<About />} /> */}
            </Routes>
        </>
    );
}

export default App;
