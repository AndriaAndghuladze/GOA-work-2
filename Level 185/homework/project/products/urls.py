from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register, name='login'),
    path('register/', views.Register, name='register'),
]