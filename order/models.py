from django.db import models
from django.contrib.auth.models import User
from .choices import Bron, Room_Type


# Create your models here.
class Order(models.Model):
    type_room = models.CharField(max_length=100, choices=Room_Type.choices)
    room_number = models.IntegerField()
    status = models.CharField(max_length=100)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_booking = models.CharField(max_length=100, choices=Bron.choices, )
    room_date = models.DateField()
    sum_of_people = models.IntegerField()

    def __str__(self):
        return self.type_room
