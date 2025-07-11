from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='room_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.room.name} — {self.date} ({self.start_time} - {self.end_time})"
