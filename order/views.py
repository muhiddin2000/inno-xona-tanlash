from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializers, OrderStatusSerializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView

from rest_framework.permissions import IsAdminUser


# Create your views here.
# POST
class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


