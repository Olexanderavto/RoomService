from django.db import models
from django.contrib.auth.models import User
from datetime import date
from .room_models import Room

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.room.name} — {self.start_date} → {self.end_date}"

