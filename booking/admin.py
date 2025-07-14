from django.contrib import admin
from .models import Room, Booking, Category  # Импортируем модели

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Category)


