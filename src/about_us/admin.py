from django.contrib import admin
from .models import PageInfo


class PageInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'desc', 'img', 'is_active']}),
        ]
    list_display = ['title', 'desc', 'img', 'is_active']
    list_filter = ['title', 'is_active']
    search_fields = ['title', ]


admin.site.register(PageInfo, PageInfoAdmin)
