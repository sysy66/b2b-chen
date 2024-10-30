from django.shortcuts import render, get_object_or_404

from .models import Item, Category


def home_page(request):
    return render(request, "products/home.html")


def all_p(request):
    items = Item.objects.all()
    return render(request, "products/all_p.html", {"items": items})


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, "products/detail.html", {"item": item})


def categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    items = category.item_set.all()
    return render(request, "products/categories.html", {"category": category, "items": items})
