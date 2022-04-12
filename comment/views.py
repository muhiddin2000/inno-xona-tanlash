from django.shortcuts import render
from order.permissions import IsAuthorOrReadOnl
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser


# Create your views here.


class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['comment', ]


class CommentCreate(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



