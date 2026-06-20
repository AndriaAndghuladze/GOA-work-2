from django.urls import path
from . import views

urlpatterns = [
    path('', views.athome_leptop, name='athome_leptop'),
    
]