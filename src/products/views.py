from django.shortcuts import render


def home_page(request):
    return render(request, "products/home.html")


def all_p(request):
    return render(request, "products/all_p.html")


def detail(request, identifier: str):
    return render(request, "products/detail.html")


def categories(request, identifier: str):
    return render(request, "products/categories.html")
