from django.contrib.auth.models import User
from rest_framework import serializers


# 🔸 Сериализатор регистрации
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)  # теперь email обязателен
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Этот email уже используется")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


# 🔸 Сериализатор пользователя (для профиля)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

