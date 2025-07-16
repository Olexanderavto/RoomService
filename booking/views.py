from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from .models import Room, Category, RoomRating

def room_list(request):
    category_id = request.GET.get('category')

    if category_id:
        rooms = Room.objects.filter(category_id=category_id)
    else:
        rooms = Room.objects.all()

    # ✅ Добавляем средний рейтинг для каждой комнаты (чтобы можно было сразу выводить в карточках)
    rooms = rooms.annotate(average_rating=Avg('ratings__rating'))

    return render(request, 'booking/room_list.html', {
        'rooms': rooms,
        'selected_category': int(category_id) if category_id else None,
        'show_navbar': True,
    })


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    source_category_id = request.GET.get('category')

    # ✅ Средний рейтинг
    average_rating = room.ratings.aggregate(avg=Avg('rating'))['avg'] or 0

    # ✅ Рейтинг пользователя (если он уже ставил)
    user_rating = None
    if request.user.is_authenticated:
        user_rating_obj = room.ratings.filter(user=request.user).first()
        user_rating = user_rating_obj.rating if user_rating_obj else None

    return render(request, 'booking/room_detail.html', {
        'room': room,
        'average_rating': round(average_rating, 1),
        'user_rating': user_rating,
        'show_navbar': False,
        'source_category_id': source_category_id,
    })


@login_required
def rate_room(request, room_id):
    """ ✅ Сохранение или обновление рейтинга комнаты """
    if request.method == 'POST':
        rating_value = int(request.POST.get('rating', 0))
        if 1 <= rating_value <= 5:
            RoomRating.objects.update_or_create(
                room_id=room_id,
                user=request.user,
                defaults={'rating': rating_value}
            )
    return redirect('room_detail', room_id=room_id)


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





