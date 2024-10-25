from django.urls import reverse

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    desc = models.TextField(blank=True)
    identifier = models.TextField(blank=True, unique=True)
    
    def __init__(self, *args, **kwargs):
        super(Category, self).__init__(*args, **kwargs)
        self.identifier = '-'.join(self.name.lower().split())
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Category, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("products:categories", args=[self.identifier])


class Item(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    desc = models.TextField(blank=True)
    img = models.ImageField(blank=True, upload_to='images/products/')
    is_popular = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    identifier = models.TextField(blank=True, unique=True)
    
    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        self.identifier = '-'.join(self.name.lower().split())
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Item, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("products:detail", args=[self.identifier])
