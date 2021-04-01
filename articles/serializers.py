from rest_framework.serializers import ModelSerializer

from .models import (
    Article,
    ArticleGallery,
    Subject,
)
from api.serializers import UserSerializer

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def get_fields(self):
        fields = super(ArticleSerializer, self).get_fields()
        fields['authors'] = UserSerializer(many=True)
        return fields

class GallerySerializer(ModelSerializer):
    class Meta:
        model = ArticleGallery
        fields = '__all__'

    def get_fields(self):
        fields = super(GallerySerializer, self).get_fields()
        fields['article'] = ArticleSerializer(many=False)
        return fields

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'