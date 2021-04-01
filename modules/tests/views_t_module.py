from django.test import TestCase, Client
from django.urls import reverse
from modules.validation import validateNone



#THIS JUST FUCKING TRASH





# class ViewSetTestCaseMethodGet(TestCase):	
# 	def custom_setup(self, object_list:list = None, list_reverse_name:str = None, detail_reverse_name:str = None, detail_instance_number:int = 0):
# 		# CREATE CLIENT INSTANCE
# 		self.client = APIClient()

# 		validateNone(
# 			# strict list - list of values that haven`t be None
# 			strict_list = (object_list,),
# 			# comparison list - list of pair values that mustn`t be both equill to None
# 			comparison_list = 
# 			(
# 				# pair values
# 				(list_reverse_name, detail_reverse_name),
# 			)
# 		)

# 		self.object_list = object_list

# 		self.detail_instance = self.object_list[detail_instance_number]

# 		self.list_url = reverse(list_reverse_name)
# 		self.detail_url = reverse(detail_reverse_name, args = [self.detail_instance.id.__str__()])

# 		# MAKE REQUESTS
# 		self.list_response = self.client.get(self.list_url)
# 		self.detail_response = self.client.get(self.detail_url)


# 	def status_code_test(self):
# 		self.assertEqual(self.list_response.status_code, 200)
# 		self.assertEqual(self.detail_response.status_code, 200)

# 	def list_response_test(self):
# 		# if something go wrong it raise AssertionError
# 		search_objects_from_datalist(
# 			'id', # search key name
# 			[obj.id.__str__() for obj in self.object_list], # value list
# 			self.list_response.json() # datalist:List[dict]
# 		)
# 	def detail_response_test(self):
# 		# compare actuall id of instance with id from api response
# 		self.assertEqual(
# 			self.detail_instance.id.__str__(),
# 			self.detail_response.json()['id']
# 		)