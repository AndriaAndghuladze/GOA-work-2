import api from "./api/axsios";
import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);
  const [task, setTask] = useState('');

  const getTasks = async () => {
    const response = await api.get('tasks/');
    setTasks(response.data);
  };

  const handleChange = (e) => {
    setTask(e.target.value);
  };

  useEffect(() => {
    getTasks();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault()
    const response = await api.post('tasks/', {
      title: task
    })
    setTasks(response.data)
  }

  const handleDelete = async (id) => {
    const task_delete =  await api.delete(`task_delete/${id}/`);
    setTasks(task_delete.data)

  };

  return (
    <>
      <form onSubmit={handleSubmit}>
        <input type="text" value={task} onChange={handleChange} />
        <button type="submit">submit</button>
      </form>
      <ul>
        {tasks.map((t) => (
          <li key={t.id}>
            {t.title} <button onClick={() => handleDelete(t.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </>
  );
}

export default App;
