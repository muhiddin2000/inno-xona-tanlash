from django.urls import path
from .views import RoomImgListView, RoomDetailView, \
    RoomImgDetailView, RoomListView

urlpatterns = [
    path('', RoomListView.as_view()),
    path('detail/<int:pk>', RoomDetailView.as_view()),
    path('img/', RoomImgListView.as_view()),
    path('img/detail/<int:pk>', RoomImgDetailView.as_view()),

]
