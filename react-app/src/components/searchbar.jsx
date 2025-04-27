import React from "react";
import { useState } from "react";

function SearchBar() {
    const [searchQuery, setSearchQuery] = useState("");
    
    const onChange = (e) => {
        e.preventDefault();
        setSearchQuery(e.target.value);
    };
      
    const onSubmit = (e) => {
        // Logic to handle the search and query the database for products that fulfill it
    };
      
    return (
        <>
            <form onSubmit={onSubmit}>
                <input 
                    onSubmit={onSubmit}
                    onChange={onChange}
                    type="text"
                    placeholder="search"
                    required
                />
            </form>
        </>
    );
}

export default SearchBar;
