from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ultra_leptop(request):
    return HttpResponse("Hello, this is the ultra_leptop view.")