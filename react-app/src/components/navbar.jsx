import React from "react";
import "./navbar.css";

import SearchBar from "./searchbar.jsx";

function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-left">
                <a href="/" className="logo">
                    VITAL
                </a>
            </div>
            <div className="navbar-center">
                <ul className="nav-links">
                    <li>
                        <a href="/catalog">catalog</a>
                    </li>
                    <li>
                        <a href="/about">about</a>
                    </li>
                </ul>
            </div>
            <div className="navbar-right">
                <SearchBar/>
                <a href="/cart" className="cart-icon">
                    <i className="fas fa-shopping-cart"></i>
                    <span className="cart-count">0</span>
                </a>
                <a href="/account" className="user-icon">
                    <i className="fas fa-user"></i>
                </a>
            </div>
        </nav>
    );
}

export default Navbar;
