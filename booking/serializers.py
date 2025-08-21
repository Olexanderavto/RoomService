from rest_framework import serializers
from .models import Category, Equipment, Room, RoomImage, Booking, RoomRating
from django.contrib.auth.models import User

# Серіалізація-це перетворення даних з об'єкта в JSON формат

# Звертаемось до моделі Category. (і так далі всі наступні)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'    # Тут поля таблиці моделі(тобто ми прописуемо до чого хочемо звертатися)


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['id', 'image', 'caption']


class RoomSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    equipment = EquipmentSerializer(many=True, read_only=True)
    images = RoomImageSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Room
        fields = [
            'id', 'name', 'category', 'capacity', 'description',
            'photo', 'equipment', 'images', 'average_rating'
        ]


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # отобразит username
    room = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'room', 'user', 'start_date', 'end_date']

        # Тут ще не вистачає методів для часу бронювання та з якого по який день
        # Щоб час початку був не раніше ніж час закінчення
        # Також не можна забронювати кімнату якщо вона кимось заброньована
        # І повині бути if


class RoomRatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # username

    class Meta:
        model = RoomRating
        fields = ['id', 'room', 'user', 'rating']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# Ще вроді як не вистачає UserRegistration С ПАРОЛЯМИ


