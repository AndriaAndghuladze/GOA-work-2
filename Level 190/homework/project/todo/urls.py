from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]