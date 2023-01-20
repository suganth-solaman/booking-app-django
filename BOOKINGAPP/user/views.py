# inbuilt module
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

# user defined module
from .forms import CustomUserCreationForm

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            if form.email_clean():
                messages.error(request, 'email already exist')
            else:
                if request.POST.get('staff') == '2':
                    form.instance.is_staff = True
                form.save()
                messages.success(request,f" {request.POST.get('username').capitalize()}, Your account created successfully! ")
                return render(request, "sign_up.html")
        else:
            messages.error(request, form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, "sign_up.html",{"form":form})

def sign_in(request):
    if request.method == 'POST':
        if request.method == "POST":
            print( request.POST,"hi")
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f" {request.POST.get('username').capitalize()}, You are signined successfully! ")
                return redirect('home')
            else:
                messages.error(request, "Username and Password mismatch")
                return redirect('sign_up')
    return redirect('home')


def sign_out(request):
    logout(request)
    messages.success(request, " You have been logged out successfully! ")
    return redirect('home')