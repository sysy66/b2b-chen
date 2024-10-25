from django.urls import path, include
from . import views

app_name = "products"
urlpatterns = [
    path('', views.all, name='all'),
    path('<str:identifier>/', views.detail, name='detail'),
    path('categories/<str:identifier>/', views.categories, name='categories'),
    
]
