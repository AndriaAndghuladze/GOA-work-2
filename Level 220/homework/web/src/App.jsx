import MainPage from "./components/MainPage"
import Login from "./components/authentication/Login"
import Register from "./components/authentication/Register"
import { createContext, useEffect, useState } from "react"
import api from "./api/axios"
import { Routes, Route } from "react-router-dom"

export const UserContext = createContext({})

function App() {
  const [currentUser, setCurrentUser] = useState(null)

  useEffect(() => {
    const getCurrentUser = async () => {
      const response = await api.get('users/me/')
      setCurrentUser(response.data)
    }
    getCurrentUser()
  }, [])

  console.log(currentUser)
  
  return (
    <UserContext.Provider value={{currentUser, setCurrentUser}}>
      <Routes>
        <Route path="/" index element={<MainPage/>}/>
        <Route path="/login" element={<Login/>}/>
        <Route path="/register" element={<Register/>}/>
      </Routes>
    </UserContext.Provider>
  )
}

export default App