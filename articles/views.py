from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework import generics
from rest_framework.viewsets import (
    ModelViewSet,
)

from .models import (
    Article,
    ArticleGallery,
    Subject,
)

from .serializers import (
    ArticleSerializer,
    GallerySerializer,
    SubjectSerializer
)
# Create your views here.

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class GalleryViewSet(ModelViewSet):
    queryset = ArticleGallery.objects.all()
    serializer_class = GallerySerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer




@csrf_exempt
def ArticleGalleryDetailView(request, pk):
    if request.method != 'GET': 
        return JsonResponse({"detail":f'{request.method.capitalize()} method don`t allowed'}, status = 405)
    
    try:
        article = Article.objects.get(pk = pk)

        # get article gallery
        gallery = article.get_gallery()

        # serialize gallery instance 
        data = GallerySerializer(article.get_gallery()).data

        status = 200

    except Article.DoesNotExist:
        data = {'detail':'Article DoesNotExist!!!'}

        status = 404
    
    # final return
    finally:
        return JsonResponse(data, status = status)
            
    