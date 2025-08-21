from django.urls import path
from . import api_views

urlpatterns = [
    path('rooms/', api_views.RoomListCreate.as_view(), name='room-list'),
    path('rooms/<int:pk>/', api_views.RoomDetail.as_view(), name='room-detail'),
    path('bookings/', api_views.BookingListCreate.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', api_views.BookingDetail.as_view(), name='booking-detail'),
    path('categories/', api_views.CategoryListCreate.as_view(), name='category-list'),
]
