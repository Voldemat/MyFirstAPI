import json
from typing import List

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

		self.article_list = [
			Article.objects.create(**Data.article_test_data),
			Article.objects.create(**Data.article_test_data_2),
		]

		self.list_response = self.client.get('/api/v1/articles/', format = 'json', content_type = 'application/json')


		self.detail_instance = self.article_list[0]
		self.detail_response = self.client.get(f'/api/v1/articles/{self.detail_instance.id.__str__()}/')


	def test_status_code(self):
		self.assertEqual(self.list_response.status_code, 200)
		self.assertEqual(self.detail_response.status_code, 200)

	def test_list_response(self):
		self.assertTrue(
			search_objects_from_datalist(
				'id', # search key name
				[article.id.__str__() for article in self.article_list], # value list
				self.list_response.json() # datalist:List[dict]
			)
		)
	def test_detail_response(self):
		self.assertEqual(
			self.detail_instance.id.__str__(),
			self.detail_response.json()['id']
		)



class GalleryViewSetTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()

		self.gallery_list = [
			Article.objects.create(**Data.article_test_data).gallery,
			Article.objects.create(**Data.article_test_data_2).gallery,
		]
		
		self.list_response = self.client.get('/api/v1/galleries/', format = 'json', content_type = 'application/json')


		self.detail_instance = self.gallery_list[0]

		self.detail_response = self.client.get(f'/api/v1/galleries/{self.detail_instance.id.__str__()}/')

	def test_status_code(self):
		self.assertEqual(self.list_response.status_code, 200)
		self.assertEqual(self.detail_response.status_code, 200)

	def test_list_response(self):
		self.assertTrue(
			search_objects_from_datalist(
				'id', # search key name
				[gallery.id.__str__() for gallery in self.gallery_list], # value list
				self.list_response.json() # datalist:List[dict]
			)
		)

	def test_detail_response(self):
		self.assertEqual(
			self.detail_instance.id.__str__(),
			self.detail_response.json()['id']
		)


class ArticleGalleryDetailViewTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()

		self.article = Article.objects.get_or_create(**Data.article_test_data)[0]

		self.response = self.client.get(f'/api/v1/articles/{self.article.id.__str__()}/gallery/')

	def test_status_code(self):
		self.assertEqual(self.response.status_code, 200)

	def test_detail_response(self):
		self.assertEqual(
			self.article.gallery.id.__str__(),
			self.response.json()['id']
		)