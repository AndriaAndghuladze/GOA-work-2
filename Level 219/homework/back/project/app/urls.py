from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from django.urls import path, include

# თავისით ქმნის საჭირო endpoint ებს viewset ისთვის
router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls))
]