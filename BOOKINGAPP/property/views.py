#inbuilt module
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import date
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm


#custom module
from .models import Photo,Property
from user.models import Book

# Create your views here.
@login_required(login_url='sign_up')
def own_property(request):
    house = Property.objects.filter(user=request.user)
    pic = {}
    for room in house:
        image = Photo.objects.filter(property=room)
        pic[room.id] = image[0].photo
    print(pic, "hi")
    #     for j in image:
    #         print(type(j.photo))
    context = {"room": house, "photo": pic}
    return render(request,"property.html",context )

@login_required(login_url='sign_up')
def add_property(request):
    if request.method == 'POST':
        data = request.POST
        user_data = request.user
        roomName = data['roomname1']
        Location = data['location1']
        startData = data['Avail-from1']
        enDate = data['Avail-to1']
        detail = {"guest":data['guest1'], "floor":data['floor1'], "bed":data['beds1'], "amenity":data['Amenities1'], "price":data['Price1'] }
        room = Property.objects.create(user=user_data, name=roomName, location=Location, start_date=startData, end_date=enDate, details=detail )
        print(room, room.id)
        image = request.FILES.get("images")
        all_image = dict(request.FILES)
        for pic in all_image['images']:
            Photo.objects.create(property=room, photo=pic)
        messages.success(request, " created successfully! ")
        return redirect('own_property')

    return render(request,'add_property.html')

@login_required(login_url='sign_up')
def rooms(request):
    house = Property.objects.all()
    image = Photo.objects.all()
    pic = {}
    for room in house:
        image = Photo.objects.filter(property =room)
        pic[room.id] = image[0].photo
    print(pic,"hi")

    context = {"room":house,"photo":pic}
    return render(request,'view_rooms.html', context)

@login_required(login_url='sign_up')
def details_view(request,pk):
    image = Photo.objects.filter(property__id=pk)
    print(image[0].photo)
    if request.method == 'POST':
        print(request.POST)
        s =request.POST['Avail-from1']
        e =request.POST['Avail-to1']
        s = s.split("-")
        e = e.split("-")
        d0 = date(int(s[0]), int(s[1]), int(s[2]))
        d1 = date(int(e[0]), int(e[1]), int(e[2]))
        delta = d1 - d0
        price = delta.days * int(image[0].property.details['price'])
        print(price,"rs")
        print(e,"dfasdfadf")
        booking_date = date.today().strftime("%m/%d/%Y")
        detail = {"booking_date":booking_date,"start":request.POST['Avail-from1'], "end":request.POST['Avail-to1'], "price":price}
        guest = Book.objects.create(user=request.user, property=image[0].property,details=detail)
        messages.success(request, f" {request.user.username.capitalize()}, Room booked successfully! ")
        return redirect('history')

    return render(request,'room_details.html',{'photos':image})

@login_required(login_url='sign_up')
def history(request):
    guest = Book.objects.filter(user=request.user)
    print(guest)
    return render(request,"history.html",{"guest":guest})

@login_required(login_url='sign_up')
def edit(request,pk):
    own = Property.objects.get(id=pk)
    if request.method == 'POST':
        data =request.POST
        own.name = data['roomname1']
        own.location = data['location1']
        own.details['guest'] = data['guest1']
        own.start_date = data['Avail-from1']
        own.end_date = data['Avail-to1']
        own.details['bed'] = data['beds1']
        own.details['amenity'] = data['Amenities1']
        own.details['price'] = data['Price1']
        own.save()
        messages.success(request, " Updated successfully! ")
        return redirect('home')
        print(request.POST)
    return render(request, 'add_property.html',{"own":own})

@login_required(login_url='sign_up')
def delete(request, pk):
    remover = Property.objects.get(id=pk)
    remover.delete()
    messages.success(request, " Deleted successfully! ")
    return redirect('own_property')

def search(request):
    if request.method == 'POST':
        data = request.POST
        searcher = Property.objects.filter(location=data['Location'])
        pic = {}
        for room in searcher:
            image = Photo.objects.filter(property=room)
            pic[room.id] = image[0].photo
        print(data, "hi")

    context = {"room": searcher, "photo": pic}
    return render(request, 'view_rooms.html', context)

