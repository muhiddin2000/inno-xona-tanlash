from django.shortcuts import render

from comment.models import Comment
from comment.serializers import CommentSerializer
from room.models import Room_Image, Room
from room.serialzers import RoomSerializers, Room_ImageSerialers
from rest_framework.generics import CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser
from order.models import Order
from order.serializers import OrderSerializers, OrderStatusSerializers
from order.permissions import IsAuthorOrReadOnl


# Create your views here.


class RoomImgCreateView(CreateAPIView):
    queryset = Room_Image.objects.all()
    serializer_class = Room_ImageSerialers
    permission_classes = (IsAdminUser,)


class RoomImgDeleteView(DestroyAPIView):
    queryset = Room_Image.objects.all()
    serializer_class = Room_ImageSerialers
    permission_classes = (IsAdminUser,)


class RoomImgUpdateView(RetrieveUpdateAPIView):
    queryset = Room_Image.objects.all()
    serializer_class = Room_ImageSerialers
    permission_classes = (IsAdminUser,)


class RoomCreateView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = (IsAdminUser,)


class RoomDeleteView(DestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = (IsAdminUser,)


class RoomUpdateView(RetrieveUpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializers
    permission_classes = (IsAdminUser,)


# PUT
class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = (IsAuthorOrReadOnl, IsAdminUser)


class OrderDeleteView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = (IsAdminUser,)


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = (IsAdminUser,)


class OrderEditView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = (IsAdminUser,)


class OrderEditStatusView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializers
    permission_classes = (IsAdminUser,)


class CommentDelete(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnl, IsAdminUser)
