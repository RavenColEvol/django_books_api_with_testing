from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.validators import FileExtensionValidator

from autoslug import AutoSlugField

def validate_book(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.split(value.name)[1]
    valid_extensions = ['.pdf', '.epub']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Book(models.Model):
    image = models.ImageField(upload_to='book', null = True, blank = True)
    pdf = models.FileField(upload_to='book', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'epub'])], null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title', unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs = {'slug':self.slug})


class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book} - {self.user.username}'

    class Meta:
        verbose_name_plural = 'Comments'