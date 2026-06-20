from django.urls import path
from . import views

urlpatterns = [
    path('', views.zoomer_leptop, name='zoomer_leptop'),
    
]