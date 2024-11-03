from django.urls import path, include
from . import views

app_name = "inquiry"
urlpatterns = [
    path('', views.inquiry_page, name='inquiry_page'),
]
