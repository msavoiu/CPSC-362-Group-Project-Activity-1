import React from "react";

function LoginForm() {
    const [state, setState] = React.useState({
        email: "",
        password: ""
    });

    const handleChange = e => {
        const value = e.target.value;
        setState({
            ...state,
            [e.target.name]: value
        });
    };

    const onSubmit = e => {
        e.preventDefault();

        const { email, password } = state;

        // const res = fetch("api/login");

        // if (res.ok) {
        //     Redirect to profile page
        // }

    }

    return (
        <div className="form-container sign-in-container">
            <form onSubmit={onSubmit}>
                <h1>Sign In</h1>
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
                {/* { !res.ok &&
                    <p>
                        Username and/or password is incorrect.
                    </p>
                } */}
                <button>Login</button>
            </form>
        </div>
    );
}

export default LoginForm;