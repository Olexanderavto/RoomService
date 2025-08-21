from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from .models import Room, Booking, Category
from .serializers import RoomSerializer, BookingSerializer, CategorySerializer
from django.db.models import Avg

class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    template_name = "booking/room_list.html"


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all().annotate(average_rating=Avg('ratings__rating'))
    serializer_class = RoomSerializer

class BookingListCreate(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

