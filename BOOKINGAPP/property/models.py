#inbuilt module
from django.db import models

#custom module

# Create your models here.
class Property(models.Model):
    user = models.ForeignKey('user.User',on_delete=models.CASCADE, default=None, null=True, blank=True)
    name = models.TextField(max_length=200)
    location = models.TextField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.JSONField(default=dict,blank=True)
    is_booked = models.BooleanField(default=False)
    feedback = models.JSONField(default=dict,blank=True)

    def __str__(self):
        return self.user.username

class Photo(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, default=None, null=True, blank=True)
    photo = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.property.name