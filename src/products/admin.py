from django.contrib import admin
from .models import Item, Category


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Description", {"fields": ["desc"], "classes": ["collapse"]}),
        ("Product Image", {"fields": ["img"]}),
        ("More Option", {"fields": ["category", "is_popular"], "classes": ["collapse"]}),
    ]
    list_display = ["name", "is_popular", "img", "category"]
    list_filter = ["name", "is_popular", "category"]
    search_fields = ["name"]


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1
    show_change_link = True


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}),
        ("Description", {"fields": ["desc"], "classes": ["collapse"]}),
    ]
    inlines = [ItemInline]
    list_display = ["name", "desc"]
    list_filter = ["name"]
    search_fields = ["name"]


# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
