from dataclasses import field
from multiprocessing import managers
from news.models import Post, User, Comment, Upvote
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data.update(author_name=user)
        return super().create(validated_data)


class UpvoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upvote
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data.update(author=user)
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, required=False)
    upvotes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("author_name", "title", "link", "comments", "upvotes_count")

    def get_upvotes_count(self, obj):
        return obj.upvotes.all().count()

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data.update(author_name=user)
        return super().create(validated_data)
