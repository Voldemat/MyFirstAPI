from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from ..models import Article, ArticleGallery, ArticleGalleryImage, Subject

from .testdata import Data


class ArticlesRouterUrlsTestCase(TestCase):
	def setUp(self):
		# SET DATA
		self.article = Article.objects.create(**Data.article_test_data)
		self.gallery = self.article.gallery

		# SET URLS PATH
		self.list_url = reverse('articles-list')
		self.api_url = settings.API_URL
		self.detail_url = reverse('articles-detail', args = [self.article.id.__str__()])
		self.detail_gallery_url = reverse('article_gallery', args = [self.article.id.__str__()])

	def test_list_url(self):
		self.assertEqual(f'/{self.api_url}articles/', self.list_url)


	def test_detail_url(self):
		self.assertEqual(f'/{self.api_url}articles/{self.article.id.__str__()}/', self.detail_url)


	def test_gallery_url(self):
		self.assertEqual(f'/{self.api_url}articles/{self.article.id.__str__()}/gallery/', self.detail_gallery_url)


class ArticlesGalleryRouterUrlsTestCase(TestCase):
	def setUp(self):
		# SET DATA
		self.article = Article.objects.create(**Data.article_test_data)
		self.gallery = self.article.gallery

		# SET URLS PATH
		self.api_url = settings.API_URL
		self.list_url = reverse('galleries-list')
		self.detail_url = reverse('galleries-detail', args = [self.gallery.id.__str__()])

	def test_list_url(self):
		self.assertEqual(f'/{self.api_url}galleries/', self.list_url)

	def test_detail_url(self):
		self.assertEqual(f'/{self.api_url}galleries/{self.gallery.id.__str__()}/', self.detail_url)


