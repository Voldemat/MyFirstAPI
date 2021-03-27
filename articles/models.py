from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.


class Subject(models.Model):
    id = models.UUIDField(
        primary_key = True,
        db_index    = True,
        editable    = False,
        default     = uuid.uuid4,
    )
    title       = models.CharField(verbose_name = 'Title', max_length = 150)

    dsc         = models.CharField(verbose_name = 'Description', max_length = 500)

    preview_img = models.ImageField(verbose_name = 'Subject Image', upload_to = 'subjects/images/')

    def __str__(self):
        return self.title


class Article(models.Model):
    id = models.UUIDField(
        default     = uuid.uuid4,
        db_index    = True,
        editable    = False,
        primary_key = True
    )
    title       = models.CharField(verbose_name = 'Title', max_length = 150)

    dsc         = models.CharField(verbose_name = 'Description', max_length = 300)

    preview_img = models.ImageField(verbose_name = 'Article Image', upload_to = 'articles/img/preview/')
    
    authors = models.ManyToManyField(get_user_model())

    text = models.TextField(verbose_name = 'Main Text')

    created_at = models.DateTimeField(verbose_name = 'Created at', auto_now_add = True)

    updated_at = models.DateTimeField(verbose_name = 'Updated at', auto_now = True)


    def __str__(self):
        return self.title

class ArticleGallery(models.Model):
    id = models.UUIDField(
        default = uuid.uuid4,
        db_index = True,
        editable = False,
        primary_key = True
    )
    article = models.ForeignKey(Article, on_delete = models.CASCADE, related_name = 'gallery')

    def __str__(self):
        return f'{self.article} Gallery ({self.id})'

class ArticleGalleryImage(models.Model):
    id = models.UUIDField(
        default = uuid.uuid4,
        db_index = True,
        editable = False,
        primary_key = True,
    )
    gallery = models.ForeignKey(ArticleGallery, on_delete = models.CASCADE, related_name = 'images')
    image = models.ImageField(verbose_name = 'Image', upload_to = 'articles/img/gallery/')

    def __str__(self):
        return f'{self.gallery} - Image {self.id}'
