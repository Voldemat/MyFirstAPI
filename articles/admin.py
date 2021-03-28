from django.contrib.admin import site
from .models import (
    Article, 
    ArticleGallery,
)
# Register your models here.

site.register(Article)
site.register(ArticleGallery)
