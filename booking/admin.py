from django.contrib import admin
from booking.models import Room, Booking, Category, RoomImage, Equipment

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]
    filter_horizontal = ('equipment',)

# Явно регистрируем ВСЕ модели
admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(Equipment)
#admin.site.register(RoomImage)     # Цю модель можно не додавати фото я додаю в моделі Rooms в адмінці