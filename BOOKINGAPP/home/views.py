from django.shortcuts import render

# Create your views here
from property.models import Photo,Property


def home_page(request):

    if request.method == "POST":
        print(request.POST)
    all = Property.objects.all()

    room1 = Photo.objects.filter(property__id=all[0].id)
    room2 = Photo.objects.filter(property__id=all[1].id)


    return render(request,"home_page.html",{"room1":room1[0], "room2":room2[0]})
