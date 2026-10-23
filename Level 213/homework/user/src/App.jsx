import api from "./api/axios"
import { useState, useEffect } from "react"

function App() {
  const [tasks, setTasks] = useState([])

  const getTasks = async () => {
    const response = await api.get('tasks/') 
    setTasks(response.data)
  }

  useEffect(() => {
    getTasks()
  }, [])

  console.log(tasks)

  return (
    <>
      
    </>
  )
}

export default App