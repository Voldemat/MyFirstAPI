from django.urls import reverse

from rest_framework.test import APIClient


from modules.validation import validateNone
from modules.utils import search_objects_from_datalist



class ViewSetTestCaseMethodGet:	
	def setUp(self):
		# CREATE CLIENT INSTANCE
		self.client = APIClient()

		self.model = self.Meta.model
		self.datalist = self.Meta.datalist
		self.object_list = []
		# CREATE DATA
		for data in self.datalist:
			obj = self.model.objects.create(**data)
			self.object_list.append(obj)

		try:
			detail_instance_id = self.Meta.detail_instance_number
		except AttributeError:
			detail_instance_id = 0

		try:
			reference_objects_name = self.Meta.reference_objects_name
		except AttributeError:
			reference_objects_name = None

		if reference_objects_name:
			for index, obj in enumerate(self.object_list):
				self.object_list[index] = getattr(obj, reference_objects_name)

		self.detail_instance = self.object_list[detail_instance_id]

		list_reverse_name = self.Meta.list_reverse_name
		detail_reverse_name = self.Meta.detail_reverse_name

		validateNone(
			# strict list - list of values that haven`t be None
			strict_list = (self.object_list,),
			# comparison list - list of pair values that mustn`t be both equill to None
			comparison_list = 
			(
				# pair values
				(list_reverse_name, detail_reverse_name),
			)
		)

		

		self.list_url = reverse(list_reverse_name)
		self.detail_url = reverse(detail_reverse_name, args = [self.detail_instance.id.__str__()])

		# MAKE REQUESTS
		self.list_response = self.client.get(self.list_url)
		self.detail_response = self.client.get(self.detail_url)


	def test_status_code(self):
		self.assertEqual(self.list_response.status_code, 200)
		self.assertEqual(self.detail_response.status_code, 200)

	def test_list_response(self):
		# if something go wrong it raise AssertionError
		search_objects_from_datalist(
			'id', # search key name
			[obj.id.__str__() for obj in self.object_list], # value list
			self.list_response.json() # datalist:List[dict]
		)
	def test_detail_response(self):
		# compare actuall id of instance with id from api response
		self.assertEqual(
			self.detail_instance.id.__str__(),
			self.detail_response.json()['id']
		)