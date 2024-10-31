from django.urls import path, include
from . import views

app_name = "products"
urlpatterns = [
    path('', views.all_p, name='all_p'),
    path('<str:slug>/', views.detail, name='detail'),
    path('categories/<str:slug>/', views.categories, name='categories'),
    
]
