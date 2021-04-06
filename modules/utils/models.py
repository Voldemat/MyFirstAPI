

def create_single_models(model, datalist:list):
	obj_list = []

	for data in datalist:
		obj = model.objects.create(**data)
		obj_list.append(obj)

	return obj_list

def create_multiple_models(model, datalist, ref_model, ref_datalist, ref_field):
	obj_list = []
	for ref_data, data in zip(ref_datalist, datalist):
		# Create reference object from ref_data
		if ref_data == None: continue
		ref_obj = ref_model.objects.create(**ref_data)

		# add this instance to main object data
		data[ref_field] = ref_obj

		# create main object
		data_for_signals = {
			ref_field:ref_obj
		}
		try:
			obj = model.objects.get(**data_for_signals)
		except:
			obj = model.objects.get_or_create(**data)[0]

		finally:
			# append object into object list
			obj_list.append(obj)

	return obj_list