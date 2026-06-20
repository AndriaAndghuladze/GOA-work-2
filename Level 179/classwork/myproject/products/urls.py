from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:id>/', views.product_info, name='product_info')
]