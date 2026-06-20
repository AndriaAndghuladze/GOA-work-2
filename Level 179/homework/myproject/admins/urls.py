from django.urls import path
from .views import admins, admin

urlpatterns = [
    path("admins/", admins),
    path("admins/<int:admins_id>/", admin),
]