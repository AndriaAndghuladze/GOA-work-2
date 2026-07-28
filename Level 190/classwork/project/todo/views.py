

from django.shortcuts import render,redirect

from .models import Task

# Create your views here.
def list_tasks(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        if title:
            task = Task.objects.create(title=title)
            task.save()
        return redirect('/todo/')
    
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/todo/')