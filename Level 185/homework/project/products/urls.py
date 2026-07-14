from django.urls import path
from . import views

urlpatterns = [
    path('', views.Register_view, name='login'),
    path('register/', views.Register_view, name='register'),
]