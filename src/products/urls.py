from django.urls import path, include
from . import views

app_name = "products"
urlpatterns = [
    path('', views.all_p, name='all_p'),
    path('<int:pk>/', views.detail, name='detail'),
    path('categories/<int:pk>/', views.categories, name='categories'),
    
]
