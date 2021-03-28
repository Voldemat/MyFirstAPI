from django.urls import path, include
# from rest_framework.routers import SimpleRouter
from articles.urls import urlpatterns as articles_urls



urlpatterns = []

urlpatterns += articles_urls