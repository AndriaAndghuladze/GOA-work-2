from django.urls import path
from . import views

urlpatterns = [
    path('', views.ultra_leptop, name='ultra_leptop'),
    
]