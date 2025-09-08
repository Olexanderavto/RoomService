from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,     # Принимает username и password.Возвращает access и refresh токены.
    TokenRefreshView,        # Принимает refresh токен.Отдаёт новый access.
    TokenVerifyView,         # Проверяет, действителен ли токен (refresh или access)
)
from booking.api.views import (
    RoomViewSet, BookingViewSet, CategoryViewSet,
    EquipmentViewSet, RoomImageViewSet, RoomRatingViewSet
)
from booking.api.views.auth_views import RegisterView, UserProfileView, LogoutView

# 🔸 Роутер для ViewSet
router = DefaultRouter()
router.register(r"rooms", RoomViewSet)
router.register(r"bookings", BookingViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"equipment", EquipmentViewSet)
router.register(r"images", RoomImageViewSet)
router.register(r"ratings", RoomRatingViewSet)

# 🔸 Маршруты авторизации
auth_patterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"), # Эти три вьюшки:(TokenObtainPairView, TokenRefreshView, TokenVerifyView) у меня не в проекте, а приходят из библиотеки djangorestframework-simplejwt. Вон там вначале в импорте в модуле
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("profile/", UserProfileView.as_view(), name="auth_profile"),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
]

# 🔸 Итоговые urlpatterns
urlpatterns = [
    path("", include(router.urls)),      # API rooms/bookings/etc
    path("auth/", include(auth_patterns)),  # API auth/*
]

