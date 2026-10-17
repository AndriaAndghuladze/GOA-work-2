from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm


# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'register.html', {
                'register_form': form
            }) 
    return render(request, 'register.html', {
        'register_form': RegisterForm()
    })