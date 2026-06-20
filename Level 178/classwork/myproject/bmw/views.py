from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bmw_models(request):
    return HttpResponse("BMW 3 Series, BMW 5 Series, BMW 7 Series, BMW X3, BMW X5, BMW M3")