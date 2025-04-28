import React from "react";
import HomepageContent from "../components/HomepageContent";

function Homepage() {
    return (
        <div>
            <img src="/splash.jpg" alt="Catalog splash" className="splash"/>
            <HomepageContent />
        </div>
    );
}

export default Homepage;
