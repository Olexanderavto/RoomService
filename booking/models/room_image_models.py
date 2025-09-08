from django.db import models
from .room_models import Room

class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='room_photos/')
    caption = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return f"Фото для {self.room.name}"

