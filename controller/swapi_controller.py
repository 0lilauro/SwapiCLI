from pprint import pprint
from .base_controller import BaseController
from services.swapi_service import SwapiService
from models.swapi_config import SwapiConfig

class SwapiController(BaseController):
    
    def __init__(self, swapi_config = None):
        super().__init__()
        self._swapi_config = None
        if swapi_config:
            self._swapi_config = swapi_config
            self.run()
        
    @property
    def swapi_config(self):
        return self._swapi_config
  
    @swapi_config.setter
    def swapi_config(self, value):
        try: 
            if type(value) is SwapiConfig:
                self._swapi_config = value
            elif value is None:
                self._search = None
            else: 
                raise TypeError("The value passed to SwapiConfig property is not a SwapiModel instance")
        except Exception as e:
            print(str(e))
    
    def run(self): 
        if self._swapi_config.help or self._swapi_config.version:
            exit()
        if self._swapi_config.get:
            swapi_service = SwapiService()
            endpoint = ""
            if self._swapi_config.schema:
                endpoint = swapi_service.build_schema_url(
                    self._swapi_config.object_swapi
                )
            else: 
                endpoint = swapi_service.build_find_url(
                    self._swapi_config.object_swapi,
                    self._swapi_config.id
                )
            params = swapi_service.build_params(
                self._swapi_config.wookiee,
                self._swapi_config.search
            )
            result = {}
            # print(params)
            try: 
                response = swapi_service.make_request(
                    endpoint,
                    params
                )
                result = response.json()
            except:
                print("An error has been occurred in the attemp to convert the search to JSON") 
            finally: 
               pprint(result)                 
                   
            
