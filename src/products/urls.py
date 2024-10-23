from django.urls import path, include
from . import views

app_name = "products"
urlpatterns = [
    path('', views.products_all, name='products_all'),
]
