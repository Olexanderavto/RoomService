from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render

ROOMS = [
    {
        'id': 1,
        'name': 'Conference Room A',
        'capacity': 70,
        'description': 'Простора конференц зала для великих зустрічей.'
    },
    {
        'id': 2,
        'name': 'Meeting Room B',
        'capacity': 20,
        'description': 'Кімната для проведення робочих мітингів.'
    },
    {
        'id': 3,
        'name': 'Executive Suite',
        'capacity': 4,
        'description': 'Приватна кімната для топ менеджерів'
    },
]


def room_list(request):
    return render(request, 'booking/room_list.html', {'rooms': ROOMS})

def room_detail(request, room_id):
    room = next((room for room in ROOMS if room['id'] == room_id), None)
    if room:
        return render(request, 'booking/room_detail.html', {'room': room})
    else:
        return JsonResponse({'error': 'Room not found'}, status=404)

# Про нас
def about_us(request):
    return render(request, 'booking/about_us.html')


