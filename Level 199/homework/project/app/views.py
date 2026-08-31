from django.shortcuts import render

# Create your views here.
def register():
    context = {
        'register_form': RegisterForm()
    }

    return render(context)