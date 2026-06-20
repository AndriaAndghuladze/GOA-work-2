from django.http import HttpResponse
from .data import admins_database

def admins(request):
    return HttpResponse(str(admins_database))


def admin(request, admins_id):
    return HttpResponse(str(admins_database[admins_id]))