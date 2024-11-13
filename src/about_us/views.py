from django.shortcuts import render, get_object_or_404, redirect
from .models import PageInfo


def view_page(request, title):
    pages = PageInfo.objects.filter(is_active=True)
    page_info = get_object_or_404(PageInfo, title=title, is_active=True)
    return render(request, "about_us/view_page.html", {"page_info": page_info, "pages": pages})


def about_us(request):
    return redirect('about_us:view_page', title='Company')
