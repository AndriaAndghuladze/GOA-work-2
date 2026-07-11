from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone, name='phone'),
    path('delete/<int:id>/', views.phone_delete, name='phone_delete'),
    path('detail/<int:id>/', views.phone_detail, name='phone_detail'),
]