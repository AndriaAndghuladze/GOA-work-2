from django.shortcuts import render

from .forms import LoginForm, ProductForm, RegisterForm, StudentForm

# Create your views here.

def login(request):
        context = {
                'loginform': LoginForm()
            }
        
        return render(request, 'login_form.html', context)


def register(request):
        context = {
                        'registerform': RegisterForm()
                    }
        
        
        return render(request, 'register_form.html', context)



def product(request):
        context = {
                        'productform': ProductForm()
                    }
        
        
        return render(request, 'product_form.html', context)


def student(request):
        context = {
                        'studentform': StudentForm()
                    }
        
        
        return render(request, 'student_form.html', context)