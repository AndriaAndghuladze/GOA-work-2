from urllib import request

from django.shortcuts import render

from .models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            return render(request, 'index.html', {'user': user})
        
        except:
            
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
        

    return render(request, 'index.html')


def log_out(request):
    User.objects.update(is_current_user=False)
    
    return render(request, 'index.html')



def edit_profile(request):
    try:
        context = {
            'current_user': User.objects.get(is_current_user=True)
        }
    except :  
        context = {
            'current_user': None
        }
        if request.method == 'POST':
            
            email = request.POST.get('user_email')
            username = request.POST.get('user_name')
            age = request.POST.get('user_age')
            password = request.POST.get('password')
            
            current_user = User.objects.get(is_current_user = True)
            
            if email != '':
                current_user.email = email
                current_user.save()
            
            if username != '':
                current_user.username = username
                current_user.save()
                
            if age != '':
                current_user.age = age
                current_user.save()
            
            if password != '':
                current_user.password = password
                current_user.save()
            
        
            return render(request, 'index.html')