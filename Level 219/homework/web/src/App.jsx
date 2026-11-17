import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import MainPage from "./component/MainPage";
import Register from "./component/Register";
import Login from "./component/Login";
  
function App() {
  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Tasks</Link>
        <Link to="/register">Register</Link>
        <Link to="/login">Login</Link>
      </nav>

      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
