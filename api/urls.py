from django.urls import path, include
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view 



swagger_view = get_swagger_view(title = settings.API_TITLE)

urlpatterns = [
    path('', include('articles.urls')),
    path('docs/', swagger_view),
]
