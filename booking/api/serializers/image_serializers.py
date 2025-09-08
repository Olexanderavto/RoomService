from rest_framework import serializers
from booking.models import RoomImage

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'caption']
