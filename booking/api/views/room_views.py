from rest_framework import viewsets
from django.db.models import Avg
from booking.models import Room
from booking.api.serializers import RoomSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().annotate(average_rating=Avg("ratings__rating"))
    serializer_class = RoomSerializer

    def get_queryset(self):
        return RoomSerializer.setup_eager_loading(super().get_queryset())
