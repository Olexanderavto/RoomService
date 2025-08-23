from rest_framework import serializers
from django.db.models import Avg
from booking.models import Room
from .category_serializers import CategorySerializer
from .equipment_serializers import EquipmentSerializer
from .image_serializers import RoomImageSerializer

class RoomSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    equipment = EquipmentSerializer(many=True, read_only=True)
    images = RoomImageSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Room
        fields = [
            'id', 'name', 'category', 'capacity', 'description',
            'photo', 'equipment', 'images', 'average_rating'
        ]

    @staticmethod
    def setup_eager_loading(queryset):
        return queryset.select_related('category').prefetch_related('equipment', 'images').annotate(
            average_rating=Avg("ratings__rating")
        )
