from django.contrib.admin import site
from .models import (
    Article, 
    ArticleGallery,
    ArticleGalleryImage,
    Subject,
)
# Register your models here.

site.register(Article)
site.register(ArticleGallery)
site.register(ArticleGalleryImage)
site.register(Subject)
