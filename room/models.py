from django.db import models

# Create your models here.
from order.choices import Room_Type, Bron


class Room(models.Model):
    type_room = models.CharField(max_length=100, choices=Room_Type.choices)
    type_of_booking = models.CharField(max_length=100, choices=Bron.choices, )
    about = models.TextField()


class Room_Image(models.Model):
    image = models.ImageField(upload_to='uploadRoom')
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
