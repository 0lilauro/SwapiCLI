import requests

class SwapiService:

    def __init__(self):
        self._base_url = "https://swapi.co/api/"

    def build_find_url(self, swapi_object, id=None):
        endpoint =  self._base_url + swapi_object + "/"
        if id is not None:
            endpoint += "{}/".format(id)
        return endpoint

    def build_schema_url(self, swapi_object):
        return self._base_url + swapi_object + "/schema"
        
    def build_params(self, wookiee=None, search=None):
        params = {}
        if wookiee:
            params['format'] = 'wookiee'
        if search is not None:
            params['search'] = search
        return params

    def make_request(self, endpoint, params={}):
        return requests.get(
            endpoint,
            params=params
        )        

    def simple_request(self, endpoint):
        return requests.get(
            endpoint,
        )        