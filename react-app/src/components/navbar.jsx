import React from "react";
import "./navbar.css";

import SearchBar from "./searchbar.jsx";
import { Link } from "react-router-dom"; /*for link in vital home page redirct Jiles*/
/*updated navcart and the Jiles */
function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-left">
                <Link to="/home" className="logo">
                    VITAL
                </Link>
            </div>
            <div className="navbar-center">
                <ul className="nav-links">
                    <li>
                        <a href="/catalog">Catalog</a>
                    </li>
                    <li>
                        <a href="/about">About</a>
                    </li>
                </ul>
            </div>
            <div className="navbar-right">
                <SearchBar />

                <div className="nav-cart">
                    <a href="/cart" className="cart-link">
                        <img
                            src="/img/cart.png"  // Make sure cart.png is inside public/img/
                            alt="Cart"
                            className="cart-image"
                        />
                        <span className="cart-count">0</span>
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
