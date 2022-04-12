from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.comment
