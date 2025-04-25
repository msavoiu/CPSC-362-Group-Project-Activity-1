import React from "react";

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
                body: JSON.stringify({ email: email, password: password }),
              });
              
            const res = response.json();
    
            alert(res.message);

            if (res.status != 200) {
                setValidLogin(false);
            } else {
                window.location.href = "/"; // redirect
            }

        } catch (error) {
            console.error(error.message);
            setValidLogin(false);
        }
    };

    return (
        <div className="form-container sign-in-container">
            <form onSubmit={onSubmit}>
                <h1>Sign In</h1>
                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    id="email"
                    value={state.email}
                    onChange={onChange}
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    id="password"
                    value={state.password}
                    onChange={onChange}
                />
                { !validLogin &&
                    <p>
                        Email and/or password is incorrect.
                    </p>
                }
                <button>Login</button>
            </form>
        </div>
    );
}

export default LoginForm;