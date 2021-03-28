from rest_framework.serializers import ModelSerializer

from .models import Article, ArticleGallery

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class GallerySerializer(ModelSerializer):
    class Meta:
        model = ArticleGallery
        fields = '__all__'