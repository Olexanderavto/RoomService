from rest_framework.routers import DefaultRouter
from booking.api.views import (
    RoomViewSet, BookingViewSet, CategoryViewSet,
    EquipmentViewSet, RoomImageViewSet, RoomRatingViewSet
)

router = DefaultRouter()
router.register(r"rooms", RoomViewSet)
router.register(r"bookings", BookingViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"equipment", EquipmentViewSet)
router.register(r"images", RoomImageViewSet)
router.register(r"ratings", RoomRatingViewSet)
