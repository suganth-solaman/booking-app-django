from django.contrib import admin

#custom module
from .models import User,Book

admin.site.register(User)
admin.site.register(Book)
