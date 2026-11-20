from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import LoginSerializer, TaskSerializer, UserSerializer
from .models import Task, User


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
    http_method_names = ['get', 'post']
    
    @action(detail=False, methods=['GET'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class LoginViewSet(ModelViewSet):
    serializer_class = LoginSerializer
    http_method_names = ['post']
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({
            'error': "Couldn't find user"
        }, status=status.HTTP_400_BAD_REQUEST)