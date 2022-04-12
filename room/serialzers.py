from rest_framework.serializers import ModelSerializer
from .models import Room, Room_Image


class RoomSerializers(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'type_room', 'type_of_booking', 'about']


class Room_ImageSerialers(ModelSerializer):
    class Meta:
        model = Room_Image
        fields = ['id', 'image', 'room_id']
