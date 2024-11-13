from django.urls import path, include
from . import views

app_name = "about_us"
urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('<str: title>/', views.view_page, name='view_page'),
]
