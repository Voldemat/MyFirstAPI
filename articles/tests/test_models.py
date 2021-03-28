from django.test import TestCase

from ..models import (
	Article,
	ArticleGallery,
	ArticleGalleryImage, 
	Subject,
)

class SubjectTestCase(TestCase):
	def setUp(self):
		self.data = {
			'title':'Space',
			'dsc':'Something cool',
			'preview_img':'dfsfd.img',
		}
		self.model = Subject.objects.create(**self.data)

	def test_content(self):
		for key in self.data:
			self.assertEqual(
				getattr(self.model, key),
				self.data[key]
			)

	def test_str_method(self):
		self.assertEqual(self.model.__str__(), self.model.title)


class ArticleTestCase(TestCase):
	def setUp(self):
		self.data = {
			'title':'Space',
			'text':'Something cool',
			'dsc':'sdfds',
			'preview_img':'dfsfd.img',
		}
		self.model = Article.objects.create(**self.data)

	def test_content(self):
		for key in self.data:
			self.assertEqual(
				getattr(self.model, key),
				self.data[key]
			)

	def test_str_method(self):
		self.assertEqual(self.model.__str__(), self.model.title)


class ArticleGalleryTestCase(TestCase):
	def setUp(self):
		article_data = {
			'title':'Another article',
			'text':'Something scool',
			'dsc':'sdsfds',
			'preview_img':'dfssfd.img',
		}
		self.article = Article.objects.create(**article_data)

		self.model = self.article.get_gallery()

	def test_contents(self):
		self.assertEqual(self.article, self.model.article)

	def test_str_method(self):
		self.assertEqual(self.model.__str__(), f'{self.article.__str__().capitalize()} -> Gallery')



class ArticleGalleryImageTestCase(TestCase):
	def setUp(self):
		article_data = {
			'title':'Another article',
			'text':'Something scool',
			'dsc':'sdsfds',
			'preview_img':'dfssfd.img',
		}
		self.gallery = Article.objects.create(**article_data).get_gallery()
		self.image = ArticleGalleryImage(gallery = self.gallery, image = 'image.img')

	def test_content(self):
		self.assertEqual(self.gallery, self.image.gallery)
		self.assertEqual(self.image.image, 'image.img')

	def test_str_method(self):
		self.assertEqual(self.image.__str__(), f'{self.image.gallery} -> Image {self.image.id}')

