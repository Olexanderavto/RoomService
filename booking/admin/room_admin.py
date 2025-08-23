from django.contrib import admin
from booking.models import Room, Booking, Category, RoomImage, Equipment

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]
    filter_horizontal = ('equipment',)

admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(Equipment)
