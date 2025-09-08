from django.urls import path, include
from booking.api import routers  # теперь тянем весь routers.py

urlpatterns = [
    # API
    path("api/", include(routers.urlpatterns)),

    # HTML-шаблоны (на будущее)
    # path("", views.index, name="index"),
    # path("profile/", views.profile, name="profile"),
]






