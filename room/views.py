from django.shortcuts import render
from .models import Room_Image, Room
from .serialzers import RoomSerializers, Room_ImageSerialers
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView


# Create your views here.

class RoomImgListView(ListAPIView):
    queryset = Room_Image.objects.all()
    serializer_class = Room_ImageSerialers


class RoomImgDetailView(RetrieveAPIView):
    queryset = Room_Image.objects.all()
    serializer_class = Room_ImageSerialers


class RoomListView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers


class RoomDetailView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
