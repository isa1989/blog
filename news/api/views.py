from django.shortcuts import render
from rest_framework import serializers, viewsets, generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from knox.models import AuthToken
from django.contrib.auth import login as auth_login


from news.models import User, Post, Comment, Upvote
from rest_framework.views import APIView


from news.api.permissions import IsOwner


from news.api.serializers import (
    PostSerializer,
    CommentSerializer,
    UpvoteSerializer,
    RegisterSerializer,
    UserSerializer,
    LoginUserSerializer,
)

import logging

logger = logging.getLogger(__name__)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = [
                permissions.IsAuthenticated,
            ]
        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [
                IsOwner,
            ]
        return super(self.__class__, self).get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = [
                permissions.IsAuthenticated,
            ]

        elif self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes = [
                IsOwner,
            ]

        return super(self.__class__, self).get_permissions()


class UpvoteViewSet(viewsets.ModelViewSet):
    queryset = Upvote.objects.all()
    serializer_class = UpvoteSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            self.permission_classes = [
                permissions.IsAuthenticated,
            ]
        elif self.action in ["destroy"]:
            self.permission_classes = [
                IsOwner,
            ]
        return super(self.__class__, self).get_permissions()


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class LoginAPIView(generics.GenericAPIView):
    queryser=Post.objects.all()
    serializer_class = LoginUserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        user = serializer.validated_data
        response = JsonResponse(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )
        return response
