import React from "react";
import "./form.css";

function LoginForm() {
    const [state, setState] = React.useState({
        email: "",
        password: ""
    });
    const [validLogin, setValidLogin] = React.useState(true);

    const onChange = (e) => {
        const value = e.target.value;
        setState({
            ...state,
            [e.target.name]: value
        });
    };

    const onSubmit = async (e) => {
        try {
            e.preventDefault();

            const { email, password } = state;
            
            const response = await fetch("http://localhost:5000/api/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                credentials: "include",
                body: JSON.stringify({ email: email, password: password }),
              });
              
            const res = response.json();

            if (response.status != 200) {
                setValidLogin(false);
            } else {
                window.location.href = "/profile"; // redirect
            }

        } catch (error) {
            console.error(error.message);
            setValidLogin(false);
        }
    };

    return (
        <>
            <form className="user-form" onSubmit={onSubmit}>
                <h1>Sign In</h1>
                <input
                    type="email"
                    name="email"
                    placeholder="email"
                    id="email"
                    value={state.email}
                    onChange={onChange}
                />
                <input
                    type="password"
                    name="password"
                    placeholder="password"
                    id="password"
                    value={state.password}
                    onChange={onChange}
                />
                { !validLogin &&
                    <p>
                        Email and/or password is incorrect.
                    </p>
                }
                <button className="button">Login</button>
            </form>
        </>
    );
}

export default LoginForm;