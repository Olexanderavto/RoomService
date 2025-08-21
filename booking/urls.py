from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm
from .views import (
    RoomListView, RoomDetailView, BookRoomView, MyBookingsView, DeleteBookingView,
    RateRoomView, AboutUsView, CategoryListView, RegisterView
)

# эндпоинти
urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'), # эндпоинти
    path('rooms/', RoomListView.as_view(), name='room_list'),
    path('rooms/<int:room_id>/', RoomDetailView.as_view(), name='room_detail'),
    path('rooms/<int:room_id>/book/', BookRoomView.as_view(), name='book_room'),
    path('my-bookings/', MyBookingsView.as_view(), name='my_bookings'),
    path('delete-booking/<int:pk>/', DeleteBookingView.as_view(), name='delete_booking'),
    path('rooms/<int:room_id>/rate/', RateRoomView.as_view(), name='rate_room'),
    path('about/', AboutUsView.as_view(), name='about_us'),

    # Аутентификация
    path('login/', auth_views.LoginView.as_view(
        template_name='booking/login.html',
        authentication_form=CustomLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]


