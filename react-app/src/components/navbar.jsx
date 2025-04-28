import React from "react";
import "./navbar.css";

import SearchBar from "./searchbar.jsx";
import { Link } from "react-router-dom";

function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-left">
                <Link to="/" className="logo">
                    VITAL
                </Link>
            </div>
            <div className="navbar-center">
                <ul className="nav-links">
                    <li>
                        <a href="/catalog">catalog</a>
                    </li>
                    <li>
                        <a href="/profile">profile</a>
                    </li>
                    <li>
                        <a href="/login">login</a>
                    </li>
                    <li>
                        <a href="/register">register</a>
                    </li>
                </ul>
            </div>
            <div className="navbar-right">
                <SearchBar />

                <div className="nav-cart">
                    <a href="/cart" className="cart-link">
                        <img
                            src="/cart.png"
                            alt="Cart"
                            className="cart-image"
                        />
                    </a>
                </div>

                <a href="/account" className="user-icon">
                    <i className="fas fa-user"></i>
                </a>
            </div>
        </nav>
    );
}

export default Navbar;
