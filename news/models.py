from django.db import models

from django.conf import settings

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Post(models.Model):
    author_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author_name"
    )
    title = models.CharField(
        max_length=255,
    )
    link = models.URLField(
        max_length=255,
    )
    creation_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author_name = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)


class Upvote(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="upvoter"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="upvotes")
