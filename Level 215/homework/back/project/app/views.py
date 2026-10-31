from .serializers import TaskSerializer
from .models import Task
from rest_framework.viewsets import ModelViewSet

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer