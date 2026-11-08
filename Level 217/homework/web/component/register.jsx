import api from "./api/axsios"
import { useState } from "react"

function Register() {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        first_name: '',
        last_name: '',
        password: ''
    })

    const handleChange = (e) => {
        setFormData({
        ...formData,
        [e.target.name]: e.target.value
        })
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        await api.post('users/', formData)
    }

    return (
        <form onSubmit={handleSubmit}>
        <input type="text" name="username" onChange={handleChange} />
        <input type="email" name="email" onChange={handleChange} />
        <input type="text" name="first_name" onChange={handleChange} />
        <input type="text" name="last_name" onChange={handleChange} />
        <input type="password" name="password" onChange={handleChange} />
        <button type="submit">submit</button>
        </form>
    )
    }

export default Register