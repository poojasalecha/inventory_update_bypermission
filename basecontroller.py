from django.http import JsonResponse
import json

""" BaseController
 For Sending http response 

"""
class BaseController(object):


    """ respond with error (in case of error)
    @param http status code, message
    @return http response with status code
    """
    def respond_with_error(self, status_code, message):
        response = {}
        response['data'] = {}
        
        response['notification'] = {}
        response['notification']['hint'] = "Error"
        response['notification']['message'] = message
        response['notification']['code'] = status_code
        response['notification']['type'] = "Failed"    
        
        response = JsonResponse(response, content_type='application/json', status=status_code)
        return response


    """ respond with success
    @param http status code, message
    @return http response with status code
    """    
    def respond_with_success(self, status_code, message, data=None):
        response = {}
        
        response['notification'] = {}
        response['notification']['hint'] = "Success"
        response['notification']['message'] = message
        response['notification']['code'] = status_code
        response['notification']['type'] = "Success"    
        
        response =  JsonResponse(response, content_type='application/json', status=status_code)
        return response

    """ respond_with_paginated_collection
    @param http status code, data, pagination data, transformer
    @return http response with status code
    """ 
    def respond_with_paginated_collection(self, status_code, data, paginated, transformer):
        response ={}
        response['data'] = self.fetch_data_from_transformer(transformer,data)
        response['pagination'] ={}
        response['pagination']['totalCount']=paginated['total_count']
        response['pagination']['totalPages']=paginated['total_pages']    
        response['pagination']['page'] =paginated['page']
        response['pagination']['item'] =paginated['item']
        response['pagination']['count'] = len(response['data'])
        response['notification'] = {}
        response['notification']['hint'] = "Response Sent"
        response['notification']['message'] = "Success"
        response['notification']['code'] = "200"
        response['notification']['type'] = "Success"    

        response =  JsonResponse(response, content_type='application/json', status=status_code)
        return response
     

    """ fetch_data_from_transformer """     
    def fetch_data_from_transformer(self, transformer, data):
        result = []
        for key, value in enumerate(data):
            result.append(transformer.transform(value))
        return result