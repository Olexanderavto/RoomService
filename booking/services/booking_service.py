from datetime import date
from booking.models import Booking, Room

def is_room_available(room: Room, start_date: date, end_date: date) -> bool:
    return not Booking.objects.filter(
        room=room,
        start_date__lte=end_date,
        end_date__gte=start_date
    ).exists()
