import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Main from "./Main";
import Register from "./Register";
import Login from "./Login";
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Tasks</Link>
        <Link to="/register">Register</Link>
        <Link to="/login">Login</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
