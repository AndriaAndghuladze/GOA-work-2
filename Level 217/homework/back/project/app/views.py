from .serializers import TaskSerializer
from .models import Task
from rest_framework.viewsets import ModelViewSet

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        print('status code 200')
        return super().list(request, *args, **kwargs)
    
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']