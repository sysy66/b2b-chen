from django.urls import reverse
from django.contrib import admin
from django.db import models
from autoslug import AutoSlugField

# TODO: real options is ?
SIZES = (
    ('General', 'General'),
    ('10mm', '10mm'),
    ('20mm', '20mm'),
    ('30mm', '30mm'),
)
THICKNESS = (
    ('General', 'General'),
    ('10mm', '10mm'),
    ('20mm', '20mm'),
    ('30mm', '30mm'),
)
COLOUR = (
    ('General', 'General'),
    ('10mm', '10mm'),
    ('20mm', '20mm'),
    ('30mm', '30mm'),
)


# TODO: models index???
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(blank=True, default='')
    slug = AutoSlugField(populate_from='name', max_length=50, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    @admin.display(description='LINK')
    def get_absolute_url(self):
        return reverse('products:categories', args=[self.slug])


class Item(models.Model):
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=50, default='General', choices=SIZES)
    thickness = models.CharField(max_length=50, default='General', choices=THICKNESS)
    colour = models.CharField(max_length=50, default='General', choices=COLOUR)
    desc = models.TextField(blank=True, default='')
    img = models.ImageField(upload_to='images/products/', default='images/products/default.jpg')
    is_popular = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='1')
    slug = AutoSlugField(populate_from='name', max_length=50, unique=True)
    
    class Meta:
        ordering = ('name',)
        unique_together = ('name', 'category', 'size', 'thickness', 'colour')
    
    def __str__(self):
        return self.name
    
    @admin.display(description='LINK')
    def get_absolute_url(self):
        return reverse('products:detail', args=[self.slug])
