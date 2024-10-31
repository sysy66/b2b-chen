import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class ClientInfo(models.Model):
    cli_company = models.CharField(max_length=100)
    cli_phone = models.CharField(max_length=15)
    cli_email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @admin.display(boolean=True)
    @property
    def was_connected_recently(self):
        return timezone.now() >= self.updated_at >= timezone.now() - datetime.timedelta(days=30)
    
    def __str__(self):
        return self.cli_company


class MessageInfo(models.Model):
    msg_subject = models.CharField(max_length=200)
    msg_text = models.TextField()
    msg_client = models.ForeignKey(ClientInfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deal = models.BooleanField(default=False)
    dealt_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.msg_subject


