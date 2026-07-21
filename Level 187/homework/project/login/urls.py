from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]