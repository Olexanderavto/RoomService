from django import forms
from booking.models import Booking
from booking.services import is_room_available

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
        labels = {'start_date': "Дата початку", 'end_date': "Дата завершення"}
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned = super().clean()
        start_date = cleaned.get('start_date')
        end_date = cleaned.get('end_date')
        room = self.initial.get('room')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Дата початку має бути меншою або рівною даті завершення.")

        if start_date and end_date and room and not is_room_available(room, start_date, end_date):
            raise forms.ValidationError("Квартира вже заброньована на вибрані дати.")

        return cleaned
