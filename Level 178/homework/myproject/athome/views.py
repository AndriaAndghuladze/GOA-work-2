from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def athome_leptop(request):
    return HttpResponse("Hello, this is the athome_leptop view.")