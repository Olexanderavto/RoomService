from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from .room_models import Room

class RoomRating(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('room', 'user')

    def __str__(self) -> str:
        return f"{self.room.name} — {self.rating}★ від {self.user.username}"

