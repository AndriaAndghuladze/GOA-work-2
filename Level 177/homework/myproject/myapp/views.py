from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def all_users(request):
    return HttpResponse("All users")


def del_users(request):
    return HttpResponse("del users")


def add_users(request):
    return HttpResponse("add users")

def change_users(request):
    return HttpResponse("change users")
