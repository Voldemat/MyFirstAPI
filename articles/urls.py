from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    ArticleViewSet,
    GalleryViewSet,

    ArticleGalleryDetailView,
)



router = SimpleRouter()

router.register('articles', ArticleViewSet, basename = 'articles')
router.register('galleries', GalleryViewSet, basename = 'galleries')

urlpatterns = [
    path('articles/<uuid:pk>/gallery/', ArticleGalleryDetailView, name = 'article_gallery'),
]
urlpatterns += router.urls