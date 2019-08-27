import unittest
from controllers.swapi_controller import SwapiController
from models.swapi_config import SwapiConfig
from models.pilot import Pilot
from models.starships import Starships

class VerifySwapiController(unittest.TestCase):

    def generate_search_response(self, valid = True, ships = True):
        response = {
            "count": 1, 
            "next": None, 
            "previous": None, 
            "results": [
                {
                    "name": "R2-D2", 
                    "height": "96", 
                    "mass": "32", 
                    "hair_color": "n/a", 
                    "skin_color": "white, blue", 
                    "eye_color": "red", 
                    "birth_year": "33BBY", 
                    "gender": "n/a", 
                    "homeworld": "https://swapi.co/api/planets/8/", 
                    "films": [
                        "https://swapi.co/api/films/2/", 
                        "https://swapi.co/api/films/5/", 
                        "https://swapi.co/api/films/4/", 
                        "https://swapi.co/api/films/6/", 
                        "https://swapi.co/api/films/3/", 
                        "https://swapi.co/api/films/1/", 
                        "https://swapi.co/api/films/7/"
                    ], 
                    "species": [
                        "https://swapi.co/api/species/2/"
                    ], 
                    "vehicles": [], 
                    "starships": [
                        'https://swapi.co/api/starships/2/',
                        'https://swapi.co/api/starships/3/'
                    ], 
                    "created": "2014-12-10T15:11:50.376000Z", 
                    "edited": "2014-12-20T21:17:50.311000Z", 
                    "url": "https://swapi.co/api/people/3/"
                }
            ]
        }
        if not valid: 
            response['count'] = 0
            response['results'] = []
        elif not ships: 
            response['results'][0]['starships'] = []
        return response

    def generate_swapi_config(self):
        arguments = {}
        arguments['get'] = True
        arguments['<object>'] = "people"
        arguments['--schema'] = False
        arguments['--wookiee'] = True
        arguments['--id'] = 1
        arguments['--search'] = False
        arguments['--help'] = False
        arguments['--version'] = False
        arguments['--fastest'] = False
        arguments['--name'] = False
        arguments['pilot'] = None

        swapi_config = SwapiConfig()
        swapi_config.read_arguments(arguments)
        return swapi_config
        
    def test_instance_property(self):
        swapi_controller_one = SwapiController()
        self.assertEqual(None, swapi_controller_one.swapi_config)
        
        swapi_controller_one = SwapiController()
        swp_config = self.generate_swapi_config()
        swapi_controller_one.swapi_config = swp_config
        self.assertEqual(swp_config, swapi_controller_one.swapi_config)
        
    def test_run_command(self):
        
        swapi_controller_one = SwapiController()
        swp_config = self.generate_swapi_config()
        swp_config.help = True
        swapi_controller_one.swapi_config = swp_config
        self.assertIsNone(swapi_controller_one.run())

        swapi_controller_two = SwapiController()
        swp_config = self.generate_swapi_config()
        swp_config.get = False
        swapi_controller_two.swapi_config = swp_config
        self.assertIsNone(swapi_controller_two.run())

        swapi_controller_three = SwapiController()
        swp_config = self.generate_swapi_config()
        swp_config.get = False
        swp_config.pilot = "luke"
        swapi_controller_three.swapi_config = swp_config
        self.assertIsNone(swapi_controller_three.run())

        swapi_controller_four = SwapiController()
        swp_config = self.generate_swapi_config()
        swapi_controller_four.swapi_config = swp_config
        self.assertIsNone(swapi_controller_four.run())

    def test_fill_starship(self):
        endpoint_right = "https://swapi.co/api/starships/9/"
        endpoint_error = "https://swapi.co/api/starships/1000002/"
        
        swapi_controller_one = SwapiController()
        response_one = swapi_controller_one.fill_starship(endpoint_right)
        self.assertIsNotNone(response_one)
        self.assertIsInstance(response_one, Starships)

        swapi_controller_two = SwapiController()
        response_two = swapi_controller_two.fill_starship(endpoint_error)
        self.assertIsNone(response_two)

    def test_fill_pilot(self):
        swapi_controller_one = SwapiController()
        pilot_one = swapi_controller_one.fill_pilot(self.generate_search_response(valid=True, ships=True)['results'][0])
        self.assertIsNotNone(pilot_one)
        self.assertIsInstance(pilot_one, Pilot)
        swapi_controller_one = SwapiController()

        swapi_controller_two = SwapiController()
        pilot_two = swapi_controller_two.fill_pilot(self.generate_search_response(valid=False))
        self.assertIsNone(pilot_two)

        swapi_controller_three = SwapiController()
        pilot_three = swapi_controller_three.fill_pilot(self.generate_search_response(valid=True, ships=False)['results'][0])
        self.assertIsNone(pilot_three)