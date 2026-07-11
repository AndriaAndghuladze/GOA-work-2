from urllib import request

from django.shortcuts import render

from .models import Phone

# Create your views here.
def phone(request):
    context = {
        'phones': Phone.objects.all()
    }
    return render(request, 'phone/phone.html', context)


def phone_delete(request, id):
    phone = Phone.objects.get(id=id)
    phone.delete()
    context = {
        'phones': Phone.objects.all()
    }
    return render(request, 'phone/phone.html', context)

def phone_detail(request, id):
    phone = Phone.objects.get(id=id)
    context = {
        'phone': phone
    }
    return render(request, 'phone/phone_detail.html', context)