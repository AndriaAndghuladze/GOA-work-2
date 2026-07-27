from django.shortcuts import render, redirect

from .utils import get_all_todos, add_todo, delete_todo

def list_tasks(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        add_todo(title)
        return redirect('list_tasks') 
        
    tasks = get_all_todos()
    return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, task_id):
    delete_todo(task_id)
    return redirect('list_tasks')  
