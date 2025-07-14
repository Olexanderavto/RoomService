from django.shortcuts import render, get_object_or_404
from .models import Room, Category

def room_list(request):
    category_id = request.GET.get('category')

    if category_id:
        rooms = Room.objects.filter(category_id=category_id)
    else:
        rooms = Room.objects.all()

    return render(request, 'booking/room_list.html', {
        'rooms': rooms,
        'selected_category': int(category_id) if category_id else None,
        'show_navbar': True,
    })


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    source_category_id = request.GET.get('category')
    return render(request, 'booking/room_detail.html', {
        'room': room,
        'show_navbar': False,
        'source_category_id': source_category_id,
    })

def about_us(request):
    return render(request, 'booking/about_us.html', {
        'show_navbar': True
    })

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'booking/category_list.html', {
        'categories': categories,
        'show_navbar': True,
    })



