from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BookAPI, CommentAPI


router = DefaultRouter()

router.register(r'books', BookAPI)
router.register(r'comments', CommentAPI)


urlpatterns = [
    path('', include(router.urls))
]