from django.shortcuts import render


def home_page(request):
    return render(request, "products/home.html")


def products_all(request):
    return render(request, "products/products_all.html")
