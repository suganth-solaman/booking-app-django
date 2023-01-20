#inbuilt module
from django.urls import path

#custom module
from . import views

urlpatterns = [
    path("",views.home_page,name="home")
]