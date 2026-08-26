from django.shortcuts import render

from .forms import loginForm, registerForm

# Create your views here.

def login(request):
        context = {
                'loginform': loginForm()
            }
        
        return render(request, 'login_form.html', context)
    

def register(request):
        context = {
                        'registerform': registerForm()
                    }
        
        
        return render(request, 'register_form.html', context)
