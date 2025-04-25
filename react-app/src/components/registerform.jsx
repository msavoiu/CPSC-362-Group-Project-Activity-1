import React from "react";

function RegisterForm() {
    const [state, setState] = React.useState({
        email: "",
        password: ""
    });
    const [validRegister, setvalidRegister] = React.useState(true);

    const handleChange = (e) => {
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

            const response = await fetch("http://localhost:5000/api/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email: email, password: password }),
              });
              
            const res = response.json();
    
            alert(res.message);

            if (res.status != 200) {
                setvalidRegister(false);
            } else {
                window.location.href = "/"; // redirect
            }

        } catch (error) {
            console.error(error.message);
            setvalidRegister(false);
        }
    };

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
                { validRegister &&
                    <p>
                        Email is already in use. Please choose a different one.
                    </p>
                }
                <button>Register</button>
            </form>
        </div>
    );
}

export default RegisterForm;