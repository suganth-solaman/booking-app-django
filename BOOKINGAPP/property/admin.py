#inbuilt module
from django.contrib import admin

#custom module
from .models import Property,Photo

admin.site.register(Property)
admin.site.register(Photo)