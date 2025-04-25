import React from "react";
import "./form.css";

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

            console.log(res.status)

            if (response.status != 201) {
                setvalidRegister(false);
            } else {
                window.location.href = "/profile"; // redirect
            }

        } catch (error) {
            console.error(error.message);
            setvalidRegister(false);
        }
    };

    return (
        <>
            <form className="user-form" onSubmit={onSubmit}>
                <h1>sign up</h1>
                <input
                    type="email"
                    placeholder="email"
                    name="email"
                    value={state.email}
                    onChange={handleChange}
                />
                <input
                    type="password"
                    name="password"
                    placeholder="password"
                    value={state.password}
                    onChange={handleChange}
                />
                { !validRegister &&
                    <p>
                        email is already in use. please choose a different one.
                    </p>
                }
                <button class="button">register</button>
            </form>
        </>
    );
}

export default RegisterForm;