import unittest
import re
from services.swapi_service import SwapiService

class VerifySwapiService(unittest.TestCase):
    def test_instance_property(self):
        service = SwapiService()
        self.assertIsNotNone(service.get)

    def test_functions(self):
        service = SwapiService()
        patter1 = r'/planets/$'
        patter2 = r'/planets/5/$'
        patter3 = r'/planets/schema$'
        
        url_one = service.build_find_url("planets")
        self.assertTrue(re.search(patter1, url_one))

        url_two = service.build_find_url("planets", 5) 
        self.assertTrue(re.search(patter2, url_two))
        
        url_three = service.build_schema_url("planets") 
        self.assertTrue(re.search(patter3, url_three))

        params_one = service.build_params()
        self.assertEqual({}, params_one)

        name = "luke"
        params_two = service.build_params(True,name)
        self.assertTrue('format' in params_two)
        self.assertTrue('search' in params_two)
        self.assertEqual("wookiee", params_two['format'])
        self.assertEqual(name, params_two['search'])

    def test_request(self):
        url = "https://swapi.co/api/"
        service = SwapiService()
        
        response = service.make_request(url, {})
        self.assertTrue(response.status_code == 200)

        response = service.make_request(url)
        self.assertTrue(response.status_code == 200)
        
        fail = False 
        try: 
            url = "https://swsdfdsfsdfdapi.co/apsdasdai/"
            response = service.make_request(url,{'bacon': 123})
        except:
            fail = True
        finally:
            self.assertTrue(fail)
        