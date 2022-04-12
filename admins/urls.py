from django.urls import path
from .views import RoomCreateView, RoomDeleteView, RoomUpdateView, \
    RoomImgCreateView, RoomImgUpdateView, RoomImgDeleteView, OrderDeleteView, OrderDetailView, OrderListView, \
    OrderEditView, OrderEditStatusView, CommentDelete

urlpatterns = [
    path('room/create/', RoomCreateView.as_view()),
    path('room/delete/<int:pk>', RoomDeleteView.as_view()),
    path('room/update/<int:pk>', RoomUpdateView.as_view()),
    path('room_img/create/', RoomImgCreateView.as_view()),
    path('room_img/delete/<int:pk>', RoomImgDeleteView.as_view()),
    path('room_img/update/<int:pk>', RoomImgUpdateView.as_view()),

    path('order/', OrderListView.as_view()),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view()),
    path('order/detail/<int:pk>/', OrderDetailView.as_view()),
    path('order/edit/<int:pk>/', OrderEditView.as_view()),
    path('order/status/<int:pk>/', OrderEditStatusView.as_view()),

    path('comment/delete/<int:pk>', CommentDelete.as_view())

]
