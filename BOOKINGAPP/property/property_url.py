#inbuilt module
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#custom module
from . import views

urlpatterns = [
    path('own_property', views.own_property, name='own_property'),
    path('add_property',views.add_property,name='add_property'),
    path('rooms', views.rooms, name='rooms'),
    path('details_view/<int:pk>', views.details_view, name='details_view'),
    path('history', views.history, name='history'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('search', views.search, name='search'),
]