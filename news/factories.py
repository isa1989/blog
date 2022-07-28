import string

import factory
from django.contrib.auth.models import Group
from factory.django import DjangoModelFactory

from news import models as nm


class MyUserFactory(DjangoModelFactory):
    class Meta:
        model = nm.User

    email = "admin@admin.com"
    username = "admin"
    password = factory.PostGenerationMethodCall("set_password", "adm1n")

    is_superuser = False
    is_staff = True
    is_active = True


class PostFactory(DjangoModelFactory):
    class Meta:
        model = nm.Post


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = nm.Comment


class UpvoteFactory(DjangoModelFactory):
    class Meta:
        model = nm.Upvote
