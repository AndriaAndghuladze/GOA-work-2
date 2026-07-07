from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bmw_list, name='bmw_list'),
    path('delete/<int:id>/', views.Bmw_delete, name='bmw_delete'),
    path('detail/<int:id>/', views.Bmw_detail, name='bmw_detail'),
]