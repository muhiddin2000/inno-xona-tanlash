from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Order


class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = ['type_room', 'id', 'room_number', 'status', 'user_id', 'type_of_booking', 'room_date',
                  'sum_of_people']


class OrderStatusSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status']
