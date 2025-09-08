from django.db import models
from .category_models import Category
from .equipment_models import Equipment

class Room(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rooms', null=True, blank=True)
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='room_photos/', blank=True, null=True)
    equipment = models.ManyToManyField(Equipment, related_name='rooms', blank=True)

    def __str__(self) -> str:
        category_name = self.category.name if self.category else "Без категории"
        return f"{self.name} ({category_name})"

