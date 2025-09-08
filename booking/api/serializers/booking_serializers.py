from rest_framework import serializers
from booking.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    room = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'room', 'user', 'start_date', 'end_date']
