
from .models import Task


def get_all_todos():
    return Task.objects.all()


def add_todo(title):
    if title and title.strip(): 
        return Task.objects.create(title=title.strip())
    return None


def delete_todo(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
