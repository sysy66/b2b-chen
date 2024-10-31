from django.shortcuts import render, get_object_or_404

from .models import Item, Category


def home_page(request):
    return render(request, "products/home.html")


def all_p(request):
    items = Item.objects.all()
    return render(request, "products/all_p.html", {"items": items})


def detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    return render(request, "products/detail.html", {"item": item})


def categories(request, slug):
    category = get_object_or_404(Category, slug=slug)
    items = category.item_set.all()
    return render(request, "products/categories.html", {"category": category, "items": items})
