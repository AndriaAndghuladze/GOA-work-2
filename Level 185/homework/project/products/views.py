from django.shortcuts import render
from .models import Register

# Create your views here.
def Register(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
    
       
        user = Register.objects.create(username=username, password=password)
        user.save()
        
        

    
    return render(request, 'form.html')