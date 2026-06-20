from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_users),
    path('delete_selected/', views.del_users),
    path('add_user/', views.add_users),
    path('change_user/', views.change_users)
]