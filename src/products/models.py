from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    
    def __str__(self):
        return self.name
    
    @property
    def identifier(self):
        return '-'.join(self.name.lower().split())


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    img = models.ImageField(blank=True, upload_to='images/products/')
    is_popular = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    @property
    def identifier(self):
        return '-'.join(self.name.lower().split())
