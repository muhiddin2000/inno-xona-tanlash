from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'comment', 'rating']
