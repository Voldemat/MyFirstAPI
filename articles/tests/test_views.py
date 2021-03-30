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
article_test_data = {
	'title':'Space',
	'text':'Something cool',
	'dsc':'sdfds',
	'preview_img':'dfsfd.img',
}
article_test_data_2 = {
	'title':'Spdace',
	'text':'Somedthing cool',
	'dsc':'sdfdds',
	'preview_img':'dfsfdd.img',
}
class ArticleViewSetTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.article_list = [
			Article.objects.create(**article_test_data),
			Article.objects.create(**article_test_data_2),

		]
		self.detail_instance = self.article_list[0]
		self.list_response = self.client.get('/api/v1/articles/', format = 'json', content_type = 'application/json')
		self.detail_response = self.client.get(f'/api/v1/articles/{self.detail_instance.id.__str__()}/')



		# self.article_list.append(
		# 	Article.objects.create(**article_test_data)
		# )


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




class GalleryViewSet(TestCase):
	pass

class ArticleGalleryDetailView(TestCase):
	pass
