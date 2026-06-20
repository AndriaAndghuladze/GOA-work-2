from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def zoomer_leptop(request):
    return HttpResponse("Hello, this is the zoomer_leptop view.")