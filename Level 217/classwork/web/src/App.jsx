import { BrowserRouter, Routes, Route, Link } from "react-router-dom"
import Main from "./Main"
import Register from "./Register"
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Tasks</Link>
        <Link to="/register">Register</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App