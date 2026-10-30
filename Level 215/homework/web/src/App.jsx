import api from "./api/axsios"
import { useState, useEffect } from "react"

function App() {
  const [tasks, setTasks] = useState([])
  const [task, setTask] = useState('')
  const [editingTaskID, setEditingTaskID] = useState(null)
  const [editingValue, setEditingValue] = useState('')

  const getTasks = async () => {
    const response = await api.get('tasks/') 
    setTasks(response.data)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const response = await api.post('tasks/', {
      title: task
    })
    setTasks(prev => [...prev, response.data])
  }
  
  const handleDelete = async (id) => {
    await api.delete(`tasks/${id}/`)
    setTasks(prev => prev.filter(tsk => tsk.id !== id))
  }
  
  useEffect(() => {
    getTasks()
  }, [])
  
  const handleEditSubmit = async (e) => {
    e.preventDefault()
    const response = await api.patch(`tasks/${editingTaskID}/`, {
      title: editingValue
    })
    setEditingTaskID(null)
    setEditingValue('')
    setTasks(prev => {
      const changeIndex = prev.findIndex(tsk => tsk.id == editingTaskID)
      prev[changeIndex] = response.data 
      return prev
    })
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input type="text" name="task" onChange={(e) => setTask(e.target.value)} />
        <button type="submit">submit</button>
      </form>
      
      <section>
        {
          tasks?.map(task => {
            return <div key={`task-${task.id}`}>
              <h2>{task.title}</h2>
              {
                editingTaskID === task.id ? <form onSubmit={handleEditSubmit}>
                  <input type="text" name="editValue" onChange={(e) => setEditingValue(e.target.value)} />
                  <button type="submit">submit</button>
                </form> : <>
                  <button onClick={() => handleDelete(task.id)}>delete</button>
                  <button onClick={() => setEditingTaskID(task.id)}>edit</button>
                </>
              }
            </div>
          })
        }
      </section>
    </>
  )
}

export default App