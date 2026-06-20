from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def audi_models(request):
    return HttpResponse("Audi Q5, Audi A4, Audi A6, Audi Q7, Audi R8, Audi TT")