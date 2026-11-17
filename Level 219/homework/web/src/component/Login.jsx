import { useState } from "react";
import api from "../api/axsios";

function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault()
        const response = await api.post('login/', { email, password })
        console.log(response.data)
    }

    return (
        <div>
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
            <div>
            <label>Email:</label>
            <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
            />
            </div>
            <div>
            <label>Password:</label>
            <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
            />
            </div>
            <button type="submit">Login</button>
        </form>
        </div>
    );
    }

export default Login;
