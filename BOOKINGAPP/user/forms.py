# inbuilt module
from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.fields import NumberInput
from django.forms.forms import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

#custom module
from .models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)
    username.widget.attrs.update({'class': 'form-control','placeholder':'@username'})
    email = forms.EmailField(label='email')
    email.widget.attrs.update({'class': 'form-control','placeholder':'username@domain.com'})
    phone = forms.IntegerField(label='phone')
    phone.widget.attrs.update({'class': 'form-control','placeholder':'Phone number'})
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password1.widget.attrs.update({'class': 'form-control','placeholder':'Password'})
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    password2.widget.attrs.update({'class': 'form-control','placeholder':'Repeat password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone']

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email).exists()
        if new:
            return True
        else:
            return False