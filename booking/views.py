from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from .models import Room, Category, RoomRating, Booking
from django.urls import reverse
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm


def room_list(request):
    category_id = request.GET.get('category')

    if category_id:
        rooms = Room.objects.filter(category_id=category_id)
    else:
        rooms = Room.objects.all()

    # ✅ Добавляем средний рейтинг для каждой комнаты (чтобы можно было сразу выводить в карточках)
    rooms = rooms.annotate(average_rating=Avg('ratings__rating'))

    # ✅ Округляем рейтинг до целого числа
    for room in rooms:
        if room.average_rating:
            room.average_rating = round(room.average_rating)

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
        'average_rating': round(average_rating),
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
        # ✅ Сохраняем category параметр при редиректе
        source_category_id = request.GET.get('category')
        if source_category_id:
            return redirect(f"{reverse('room_detail', args=[room_id])}?category={source_category_id}")
        else:
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

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    existing_bookings = Booking.objects.filter(room=room).order_by('start_date')

    if request.method == 'POST':
        form = BookingForm(request.POST, initial={'room': room})
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            booking.save()
            messages.success(request, "Бронювання успішно створено!")
            return redirect('my_bookings')
    else:
        form = BookingForm(initial={'room': room})

    return render(request, 'booking/book_room.html', {
        'room': room,
        'form': form,
        'existing_bookings': existing_bookings,
        'show_navbar': True
    })



@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).select_related('room')
    return render(request, 'booking/my_bookings.html', {
        'bookings': bookings,
        'show_navbar': True
    })

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Бронювання видалено.")
        return redirect('my_bookings')

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Реєстрація успішна! Тепер увійдіть у систему.")
            return redirect('login')
    else:
        form = CustomRegisterForm()

    return render(request, 'booking/register.html', {
        'form': form,
        'show_navbar': True
    })





