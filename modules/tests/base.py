from django.test import Client
from django.urls import reverse

from modules.utils import create_single_models,create_multiple_models

class Request:
    def __init__(self, url:str = None, method:str = 'GET', data:dict = None):
        self.client = Client()
        self.url = url
        self.method = method.lower()
        self.data = data

    def get_response(self):
        response = getattr(self.client, self.method)(path = self.url, data = self.data)
        return response

class RequestReverse(Request):
    def __init__(self, reverse_name, reverse_args = None, *args, **kwargs):
        kwargs['url'] = reverse(reverse_name, args = reverse_args if reverse_args else [])
        super(RequestReverse, self).__init__(*args, **kwargs)

class BaseModelViewTestCase:
    def setUp(self):
        _meta = self.Meta

        
        model = _meta.model
        datalist = _meta.datalist
        # if datalist

        try:
            ref_model = _meta.ref_model
        except:
            ref_model = None
        
        try:
            ref_datalist = _meta.ref_datalist
        except:
            if ref_model:
                raise ValueError('Ref model set but ref_datalist not!!!')
            ref_datalist = None
        
        try:
            ref_field = _meta.ref_field
        except:
            if ref_model:
                raise ValueError('Ref model set but ref_field not!!!')
            ref_field = None
        
        self.object_list = self.get_models(model = model, ref_model = ref_model, datalist = datalist, ref_datalist = ref_datalist, ref_field = ref_field)
        
        self.response_list = []
        for request in _meta.requests_list:
            self.response_list.append(request.get_response())




    def get_models(self, model, datalist, ref_datalist = None, ref_model = None, ref_field = None):
        if model == None or datalist == None:
            return []

        if ref_datalist == None or ref_model == None or ref_field == None:
            return create_single_models(model, datalist)

        return create_multiple_models(model, datalist, ref_model, ref_datalist, ref_field)


    def test_status_codes(self):
        for response in self.response_list:
            self.assertTrue(response.status_code < 400,
            msg = f'Status code = {response.status_code}, url = {response.request["PATH_INFO"]}')