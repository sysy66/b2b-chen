from django.shortcuts import render, get_object_or_404, redirect
from .models import PageInfo


def view_page(request, title):
    page_info = get_object_or_404(PageInfo, title=title)
    return render(request, "about_us/view_page.html", {"page_info": page_info})


def about_us(request):
    return redirect('about_us:view_page', title='Company')
