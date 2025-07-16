from django.contrib import admin
from .models import Room, Booking, Category, RoomImage, Equipment

class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomImageInline]
    filter_horizontal = ('equipment',)

admin.site.register(Room, RoomAdmin)
admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(Equipment)




