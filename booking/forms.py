from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Booking
from datetime import timedelta

# ✅ Бронирование (ваш старый код)
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
        labels = {
            'start_date': "Дата початку",
            'end_date': "Дата завершення"
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        room = self.initial.get('room')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Дата початку має бути меншою або рівною даті завершення.")

        if start_date and end_date and room:
            conflicts = Booking.objects.filter(
                room=room,
                start_date__lte=end_date,
                end_date__gte=start_date
            )
            if conflicts.exists():
                raise forms.ValidationError("Квартира вже заброньована на вибрані дати.")

        return cleaned_data


# ✅ Логин
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control w-100',
            'placeholder': "Ім'я користувача"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control w-100',
            'placeholder': "Пароль"
        })
    )


# ✅ Регистрация (важно!)
class CustomRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control w-100',
            'placeholder': "Введіть ім'я користувача"
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control w-100',
            'placeholder': "Введіть пароль"
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control w-100',
            'placeholder': "Повторіть пароль"
        })
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
