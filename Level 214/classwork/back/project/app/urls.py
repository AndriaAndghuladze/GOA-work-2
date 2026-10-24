from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_view),
    path('task_delete/<int:pk>/', views.task_delete_view),
]