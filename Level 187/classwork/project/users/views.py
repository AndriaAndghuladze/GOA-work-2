from django.shortcuts import render

from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User(username=username, email=email, password=password)
        user.save()


    return render(request, 'register.html')    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            return render(request, 'index.html', {'user': user})
        
        except:
            
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
        

    return render(request, 'login.html')    