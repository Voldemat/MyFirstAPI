from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Article, ArticleGallery

@receiver(post_save, sender = Article)
def add_gallery_to_article(sender, instance, created, *args, **kwargs):
    # if article is new
    if created:
        gallery = ArticleGallery.objects.create(article = instance)