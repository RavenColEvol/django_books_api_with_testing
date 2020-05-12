from rest_framework import serializers, viewsets
from django.conf import settings

from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from .models import Book, Comment

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BookSerializer(TaggitSerializer, serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)
    tags = TagListSerializerField()

    class Meta:
        model = Book
        fields = '__all__'


