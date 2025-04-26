import React from "react";

function RegisterForm() {
    const [state, setState] = React.useState({
        email: "",
        password: ""
    });

    const message = "";

    const handleChange = (e) => {
        const value = e.target.value;
        setState({
            ...state,
            [e.target.name]: value
        });
    };

    const onSubmit = (e) => {
        e.preventDefault();

        const { email, password } = state;

        const res = fetch("api/register");

        if (res.ok) {
            // Redirect to profile page
        }

    }

    return (
        <div className="form-container sign-in-container">
            <form onSubmit={onSubmit}>
                <h1>Sign Up</h1>
                <input
                    type="email"
                    placeholder="Email"
                    name="email"
                    value={state.email}
                    onChange={handleChange}
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    value={state.password}
                    onChange={handleChange}
                />
                <button>Register</button>
            </form>
        </div>
    );
}

export default RegisterForm;