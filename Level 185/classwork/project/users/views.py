from django.shortcuts import render
from users.models import User  

def Login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
    
       
        user = User.objects.create(username=username, password=password, email=email)
        user.save()
        
        

    
    return render(request, 'form.html')