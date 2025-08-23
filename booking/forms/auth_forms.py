from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': "Ім'я користувача"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-100', 'placeholder': "Пароль"}))

class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': "Введіть ім'я користувача"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-100', 'placeholder': "Введіть пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control w-100', 'placeholder': "Повторіть пароль"}))

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
