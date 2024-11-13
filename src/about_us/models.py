from django.db import models
from django.urls import reverse


class PageInfo(models.Model):
    title = models.CharField(max_length=200, unique=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='about_us')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('about_us:view_page', args=[self.title])
    