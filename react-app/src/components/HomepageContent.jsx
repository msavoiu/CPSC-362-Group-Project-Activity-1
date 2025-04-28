import React from "react";

function HomepageContent() {
    return (
        <div className="homepage">
            <h1>Welcome to Vital</h1>
            <p>Explore our latest collection and find your fit.</p>
            <button
                onClick={() => window.location.href = "/catalog"}
                className="button">
                Shop Now
            </button>
        </div>
    );
}

export default HomepageContent;
