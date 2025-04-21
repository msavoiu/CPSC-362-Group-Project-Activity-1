import { useState } from "react"
import "./App.css"
import { Routes, Route } from "react-router-dom";

// Page components
import Login from "./pages/login.jsx";
import Navbar from "./components/navbar.jsx"

function App() {
    const [count, setCount] = useState(0)

    return (
        <>
            <Navbar />
            <Routes>
                {/* <Route path="/" element={<Home />} /> */}
                <Route path="/login" element={<Login />} />
                {/* <Route path="/register" element={<Register />} />
                <Route path="/products" element={<Catalog />} />
                <Route path="/about" element={<About />} /> */}
            </Routes>
        </>
    );
}

export default App;
