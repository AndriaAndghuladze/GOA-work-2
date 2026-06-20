from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mercedes_models(request):
    return HttpResponse("Mercedes C-Class, Mercedes E-Class, Mercedes S-Class, Mercedes GLC, Mercedes GLE, Mercedes AMG")