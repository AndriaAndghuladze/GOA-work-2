from django.urls import path
from . import views

urlpatterns = [
    path('', views.mercedes_models),
    
]