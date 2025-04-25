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

            if (res.status != 201) {
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
        <div className="form-container sign-in-container">
            <form onSubmit={onSubmit}>
                <h1>sign ip</h1>
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
                <button>register</button>
            </form>
        </div>
    );
}

export default RegisterForm;