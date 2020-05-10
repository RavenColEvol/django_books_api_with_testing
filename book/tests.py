from PIL import Image
import tempfile

from django.urls import reverse
from django.test import override_settings
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Book, Comment

def generateImage():
    image = Image.new('RGB', (100, 100))
    temp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(temp_file, 'jpeg')
    temp_file.seek(0)
    return temp_file

def create_user():
    user = get_user_model().objects.create(username='test@gmail.com', password='test@1234')
    return user


class BookTest(APITestCase):
    
    def test_can_get_books_list(self):
        books = [
            Book.objects.create(title='Django', description='django book'),
        ]
   
        response = self.client.get(reverse('book-list'))
        
        exp_books_id = [book.id for book in books]
        act_books_id = [ book.get('id') for book in response.data]
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(exp_books_id, act_books_id)
    
    def test_can_get_book_detail(self):
        book = Book.objects.create(title='Django', description='django book')
    
        response = self.client.get(book.get_absolute_url())
    
        self.assertEqual(book.title, response.data.get('title'))
        self.assertEqual(book.description, response.data.get('description'))

    @override_settings(MEDIA_ROOT=tempfile.TemporaryDirectory(prefix='mediatest').name)
    def test_user_can_create_book(self):
        data = {
            'title':'Django',
            'description':'django book',
            'image': generateImage()
        }

        response = self.client.post(reverse('book-list'), data, format='multipart')
        
        self.assertEqual( response.status_code, status.HTTP_201_CREATED)
        self.assertEqual( data.get('title'), response.data.get('title'))
        self.assertEqual( data.get('description'), response.data.get('description'))

    def test_user_can_create_comment(self):
        user = create_user()
        