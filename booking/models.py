from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rooms', null=True, blank=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='room_photos/', blank=True, null=True)
    equipment = models.ManyToManyField(Equipment, related_name='rooms', blank=True)

    def __str__(self):
        category_name = self.category.name if self.category else "Без категории"
        return f"{self.name} ({category_name})"


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='room_photos/')
    caption = models.CharField(max_length=100, blank=True, null=True)  # Описание фото (опционально)

    def __str__(self):
        return f"Фото для {self.room.name}"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()

    def __str__(self):
        return f"{self.room.name} — {self.start_date} → {self.end_date}"


class RoomRating(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = ('room', 'user')  # один пользователь = одна оценка

    def __str__(self):
        return f"{self.room.name} — {self.rating}★ від {self.user.username}"