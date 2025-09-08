from rest_framework import serializers
from booking.models import RoomRating

class RoomRatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = RoomRating
        fields = ['id', 'room', 'user', 'rating']
