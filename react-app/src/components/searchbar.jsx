import React, { useState } from "react";

function SearchBar() {
    const [searchQuery, setSearchQuery] = useState("");
    const [searchResults, setSearchResults] = useState([]);
    const [error, setError] = useState(null);

    const onChange = (e) => {
        setSearchQuery(e.target.value);
    };

    const onSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch("http://localhost:5000/api/search", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ keyword: searchQuery }),
            });

            if (!response.ok) {
                if (response.status === 404) {
                    setSearchResults([]);
                    setError("No matching items found.");
                } else {
                    throw new Error("Failed to fetch search results.");
                }
            } else {
                const data = await response.json();
                setSearchResults(data.results);
                setError(null);
            }
        } catch (err) {
            setError(err.message);
            setSearchResults([]);
        }
    };

    return (
        <>
            <form onSubmit={onSubmit}>
                <input
                    onChange={onChange}
                    type="text"
                    placeholder="search"
                    value={searchQuery}
                    required
                />
                <button className="button" type="submit">go</button>
            </form>
            {error && <p>{error}</p>}
            <ul>
                {searchResults.map((item) => (
                    <li key={item.product_id}>
                        {item.description} - {item.color} - {item.size} ({item.quantity} in stock)
                    </li>
                ))}
            </ul>
        </>
    );
}

export default SearchBar;