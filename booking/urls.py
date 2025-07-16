from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
    path('rooms/<int:room_id>/rate/', views.rate_room, name='rate_room'),
    path('about/', views.about_us, name='about_us'),
]