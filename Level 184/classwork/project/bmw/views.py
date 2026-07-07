from urllib import request

from django.shortcuts import render
from .models import Bmw
# Create your views here.

def Bmw_list(request):
    context = {
        'car': Bmw.objects.all()
    }

    return render(request, 'index.html', context)

def Bmw_delete(request, id):
    delete = Bmw.objects.get(id = id)
    delete.delete()

    return render(request, 'index.html', {'car': Bmw.objects.all()})

def Bmw_detail(request, id):
    detail = Bmw.objects.get(id = id)

    return render(request, 'detail.html', {'car': detail})