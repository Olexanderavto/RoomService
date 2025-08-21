from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db.models import Avg
from .models import Room, Category, RoomRating, Booking
from .forms import BookingForm, CustomRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404


# ✅ Список комнат
class RoomListView(ListView):
    model = Room
    template_name = 'booking/room_list.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        category_id = self.request.GET.get('category')
        qs = Room.objects.all().annotate(average_rating=Avg('ratings__rating'))
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.request.GET.get('category')
        context['selected_category'] = int(category_id) if category_id else None
        context['show_navbar'] = True
        return context


# ✅ Детали комнаты
class RoomDetailView(DetailView):
    model = Room
    template_name = 'booking/room_detail.html'
    context_object_name = 'room'
    pk_url_kwarg = 'room_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = self.object
        avg_rating = room.ratings.aggregate(avg=Avg('rating'))['avg'] or 0
        context['average_rating'] = round(avg_rating)
        if self.request.user.is_authenticated:
            user_rating_obj = room.ratings.filter(user=self.request.user).first()
            context['user_rating'] = user_rating_obj.rating if user_rating_obj else None
        context['show_navbar'] = False
        context['source_category_id'] = self.request.GET.get('category')
        return context


# ✅ Оценка комнаты
class RateRoomView(LoginRequiredMixin, TemplateView):
    def post(self, request, room_id):
        rating_value = int(request.POST.get('rating', 0))
        if 1 <= rating_value <= 5:
            RoomRating.objects.update_or_create(
                room_id=room_id,
                user=request.user,
                defaults={'rating': rating_value}
            )
        source_category_id = request.GET.get('category')
        if source_category_id:
            return redirect(f"{reverse('room_detail', args=[room_id])}?category={source_category_id}")
        return redirect('room_detail', room_id=room_id)


# ✅ О нас
class AboutUsView(TemplateView):
    template_name = 'booking/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_navbar'] = True
        return context


# ✅ Список категорий
class CategoryListView(ListView):
    model = Category
    template_name = 'booking/category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_navbar'] = True
        return context


# ✅ Бронирование комнаты
class BookRoomView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/book_room.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'room': get_object_or_404(Room, id=self.kwargs['room_id'])}
        return kwargs

    def form_valid(self, form):
        form.instance.room = get_object_or_404(Room, id=self.kwargs['room_id'])
        form.instance.user = self.request.user
        messages.success(self.request, "Бронювання успішно створено!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('my_bookings')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        room = get_object_or_404(Room, id=self.kwargs['room_id'])
        context['room'] = room
        context['existing_bookings'] = Booking.objects.filter(room=room).order_by('start_date')
        context['show_navbar'] = True
        return context


# ✅ Мои бронирования
class MyBookingsView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/my_bookings.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).select_related('room')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_navbar'] = True
        return context


# ✅ Удаление брони
class DeleteBookingView(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('my_bookings')
    template_name = 'booking/delete_booking.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Бронювання видалено.")
        return super().delete(request, *args, **kwargs)


# ✅ Регистрация
class RegisterView(CreateView):
    form_class = CustomRegisterForm
    template_name = 'booking/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, "Реєстрація успішна! Тепер увійдіть у систему.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_navbar'] = True
        return context



