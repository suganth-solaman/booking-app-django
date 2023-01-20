# inbuilt modules
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.IntegerField(default=None, null=True, blank=True)


class Book(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True, blank=True)
    property = models.ForeignKey("property.Property",on_delete=models.CASCADE, default=None, null=True, blank=True)
    details = models.JSONField(default=dict,blank=True)