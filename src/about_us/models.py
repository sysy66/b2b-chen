from django.db import models


class PageInfo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='about_us')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    