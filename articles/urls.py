
from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    ArticleViewSet,
    GalleryViewSet,
    SubjectViewSet,

    ArticleGalleryDetailView,

    check,
    static_page
)



router = SimpleRouter()

router.register('articles', ArticleViewSet, basename = 'articles')
router.register('galleries', GalleryViewSet, basename = 'galleries')
router.register('subjects', SubjectViewSet, basename = 'subjects')

urlpatterns = [
    path('articles/<uuid:pk>/gallery/', ArticleGalleryDetailView, name = 'article_gallery'),
    path('check/', check, name = 'check'),
    path('static_page/', static_page),
]
urlpatterns += router.urls