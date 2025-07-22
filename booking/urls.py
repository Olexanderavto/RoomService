from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('rooms/<int:room_id>/book/', views.book_room, name='book_room'),  # ✅ новое
    path('my-bookings/', views.my_bookings, name='my_bookings'),  # ✅ новое
    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),  # ✅ новое
    path('rooms/<int:room_id>/rate/', views.rate_room, name='rate_room'),
    path('about/', views.about_us, name='about_us'),

    # ✅ ДОБАВЛЯЕМ ВАЖНОЕ
    path('login/', auth_views.LoginView.as_view(template_name='booking/login.html',authentication_form=CustomLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),

]
