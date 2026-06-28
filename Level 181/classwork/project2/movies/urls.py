from django.urls import path
from . import views

urlpatterns = [
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/', views.all_movies, name='all_movies'),
]