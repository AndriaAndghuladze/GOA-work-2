from django.urls import path
from . import views

urlpatterns = [
    path('', views.alta_leptop, name='alta_leptop'),
    
]