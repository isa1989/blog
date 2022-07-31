from dataclasses import field
from django.contrib.auth import authenticate

from news.models import Post, User, Comment, Upvote
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class LoginUserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        user = authenticate(**data)

        if user and user.is_active:
            return user

        raise serializers.ValidationError("Unable to log in with provided credentials.")


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}


class CommentSerializer(serializers.ModelSerializer):
    author_name = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data.update(author_name=user)
        return super().create(validated_data)


class UpvoteSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Upvote
        fields = "__all__"

    def validate_post(self, value):
        if Upvote.objects.filter(post=value).exists():
            raise serializers.ValidationError("You upvoted")

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data.update(author=user)
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author_name = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, required=False)
    upvotes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("author_name", "title", "link", "comments", "upvotes_count")
        

    def validate(self,data):
        if Post.objects.filter(**data).exists():
            raise serializers.ValidationError("This post is alredy exists!")

    def get_upvotes_count(self, obj):
        return obj.upvotes.all().count()

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data.update(author_name=user)
        return super().create(validated_data)
