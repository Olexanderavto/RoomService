from django.urls import path, include
from booking.api.routers import router

urlpatterns = [
    path("api/", include(router.urls)),
]






