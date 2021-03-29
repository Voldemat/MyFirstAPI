import json
from typing import List

from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APIRequestFactory, APIClient

from ....modules.utils import search_objects_from_datalist

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
		self.response = self.client.get('/api/v1/articles/', format = 'json', content_type = 'application/json')
		self.data = self.response.json()


	def test_status_code(self):
		self.assertEqual(self.response.status_code, 200)

	def test_content(self):
		self.assertTrue(
			search_objects_from_datalist(
				'id', # search key name
				[self.article.id.__str(),], # value list
				self.data # datalist:List[dict]
			)
		)


class GalleryViewSet(TestCase):
	pass

class ArticleGalleryDetailView(TestCase):
	pass
