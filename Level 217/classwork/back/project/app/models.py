from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.TextField()


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

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