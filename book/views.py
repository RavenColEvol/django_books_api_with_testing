from rest_framework.viewsets import ModelViewSet

from .serializers import BookSerializer, CommentSerializer
from .models import Book, Comment


class BookAPI(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'slug'


class CommentAPI(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer