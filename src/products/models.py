from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib import admin
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    desc = models.TextField(blank=True)
    identifier = models.TextField(blank=True, unique=True)
    
    def __str__(self):
        return self.name
    
    def full_clean(self, *args, **kwargs):
        self.identifier = '-'.join(self.name.lower().split())
        try:
            Category.objects.get(identifier=self.identifier)
        except:
            pass
        else:
            raise ValidationError("This category has already been created")
        super(Category, self).full_clean(*args, **kwargs)
    
    @admin.display(description='LINK')
    def get_absolute_url(self):
        return reverse("products:categories", args=[self.identifier])


class Item(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    desc = models.TextField(blank=True)
    img = models.ImageField(blank=True, upload_to='images/products/')
    is_popular = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    identifier = models.TextField(blank=True, unique=True)
    
    def __str__(self):
        return self.name
    
    def full_clean(self, *args, **kwargs):
        self.identifier = '-'.join(self.name.lower().split())
        try:
            Item.objects.get(identifier=self.identifier)
        except:
            pass
        else:
            raise ValidationError("This Item has already been created")
        super(Item, self).full_clean(*args, **kwargs)
    
    @admin.display(description='LINK')
    def get_absolute_url(self):
        return reverse("products:detail", args=[self.identifier])
