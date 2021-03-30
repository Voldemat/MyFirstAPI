from typing import List, Optional
from colorama import Fore, Style

def search_objects_from_datalist(key_name:str, value_list:list, datalist:List[dict]) -> Optional[bool]:
	for obj in datalist:
		try:
			# try get the property value from obj
			key_value = obj[key_name]
		
		except:
			# if obj don`t have given key raise ValueError
			raise ValueError(f'Object from datalist don`t have {key_name} key ,\n\
								{key_name} not in {obj}')

		else:
			if key_value in value_list:

				# if key value in value list delete it
				value_list.remove(key_value)

				# if no other values in value_list return True
				if len(value_list) == 0: return True

	# if some element don`t in datalist return False
	error = '\n'
	for value in value_list:
		error += (value + Fore.RED + '            Not in datalist \n' + Style.RESET_ALL)
	raise AssertionError(error)