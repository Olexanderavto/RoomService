from rest_framework import viewsets
from booking.models import RoomImage
from booking.api.serializers import RoomImageSerializer

class RoomImageViewSet(viewsets.ModelViewSet):
    queryset = RoomImage.objects.all()
    serializer_class = RoomImageSerializer
