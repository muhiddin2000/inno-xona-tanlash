from django.contrib import admin
from .models import Room, Room_Image


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_room', 'type_of_booking', 'about']


@admin.register(Room_Image)
class Room_ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'room_id']
