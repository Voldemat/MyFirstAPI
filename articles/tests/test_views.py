import json

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APIRequestFactory, APIClient

from modules.utils import search_objects_from_datalist

from ..models import (
	Article,
	ArticleGallery,
	ArticleGalleryImage, 
	Subject,
)

from ..views import (
	ArticleViewSet,
	GalleryViewSet,
	ArticleGalleryDetailView,
)

from .testdata import Data



class ArticleViewSetTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()

		# SET DATA
		self.article_list = [
			Article.objects.create(**Data.article_test_data),
			Article.objects.create(**Data.article_test_data_2),
		]
		self.detail_instance = self.article_list[0]

		# SET URLS PATH
		list_url = reverse('articles-list')
		detail_url = reverse('articles-detail', args = [self.detail_instance.id.__str__()])

		# MAKE REQUESTS
		self.list_response = self.client.get(list_url, format = 'json', content_type = 'application/json')
		
		self.detail_response = self.client.get(detail_url)


	def test_status_code(self):
		self.assertEqual(self.list_response.status_code, 200)
		self.assertEqual(self.detail_response.status_code, 200)

	def test_list_response(self):
		# if something go wrong it raise AssertionError
		search_objects_from_datalist(
			'id', # search key name
			[obj.id.__str__() for obj in self.article_list], # value list
			self.list_response.json() # datalist:List[dict]
		)
	def test_detail_response(self):
		# compare actuall id of instance with id from api response
		self.assertEqual(
			self.detail_instance.id.__str__(),
			self.detail_response.json()['id']
		)



class GalleryViewSetTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()

		# SET DATA
		self.gallery_list = [
			Article.objects.create(**Data.article_test_data).gallery,
			Article.objects.create(**Data.article_test_data_2).gallery,
		]
		self.detail_instance = self.gallery_list[0]

		# SET URLS PATH
		list_url = reverse('galleries-list')
		detail_url = reverse('galleries-detail', args = [self.detail_instance.id.__str__()])
		
		# MAKE REQUESTS
		self.list_response = self.client.get(list_url)

		self.detail_response = self.client.get(detail_url)

	def test_status_code(self):
		self.assertEqual(self.list_response.status_code, 200)
		self.assertEqual(self.detail_response.status_code, 200)

	def test_list_response(self):
		# if something go wrong it raise AssertionError
		search_objects_from_datalist(
			'id', # search key name
			[obj.id.__str__() for obj in self.gallery_list], # value list
			self.list_response.json() # datalist:List[dict]
		)

	def test_detail_response(self):
		# compare actuall id of instance with id from api response
		self.assertEqual(
			self.detail_instance.id.__str__(),
			self.detail_response.json()['id']
		)


class ArticleGalleryDetailViewTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()

		# SET DATA
		self.article = Article.objects.get_or_create(**Data.article_test_data)[0]

		# SET URLS PATH
		url = reverse('articles-list') + self.article.id.__str__() + '/gallery/'
		
		# MAKE REQUESTS
		self.response = self.client.get(url)

	def test_status_code(self):
		self.assertEqual(self.response.status_code, 200)

	def test_detail_response(self):
		# compare actuall id of instance with id from api response
		self.assertEqual(
			self.article.gallery.id.__str__(),
			self.response.json()['id']
		)

