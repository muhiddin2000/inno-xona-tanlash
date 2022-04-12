from django.urls import path
from .views import CommentList, CommentCreate

urlpatterns = [
    path('', CommentList.as_view()),
    path('create/', CommentCreate.as_view()),

]
