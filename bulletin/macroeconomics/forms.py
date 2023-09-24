from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        # widgets = {
        #     "email": forms.TextInput(attrs={"style": "width: 1000px"}),
        #     "password1": forms.TextInput(attrs={"style": "width: 1000px"})
        # }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    