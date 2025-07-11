from django.shortcuts import render, get_object_or_404
from .models import Room

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'booking/room_list.html', {
        'rooms': rooms,
        'show_navbar': True
    })

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'booking/room_detail.html', {
        'room': room,
        'show_navbar': False
    })

def about_us(request):
    return render(request, 'booking/about_us.html', {
        'show_navbar': True
    })



