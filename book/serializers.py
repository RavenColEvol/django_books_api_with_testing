from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model

from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from .models import Book, Comment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'id')


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
