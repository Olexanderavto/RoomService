from rest_framework import viewsets
from booking.models import RoomRating
from booking.api.serializers import RoomRatingSerializer

class RoomRatingViewSet(viewsets.ModelViewSet):
    queryset = RoomRating.objects.all()
    serializer_class = RoomRatingSerializer
