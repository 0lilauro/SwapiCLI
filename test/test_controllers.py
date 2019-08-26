import unittest
from controllers.swapi_controller import SwapiController
from models.swapi_config import SwapiConfig

class VerifySwappiController(unittest.TestCase):
    def test_instance_property(self):

        swapi_controller_one = SwapiController()
        self.assertEqual(None, swapi_controller_one)
        
        swapi_controller_one.swapi_config = 100 
        self.assertEqual(None, swapi_controller_one.swapi_config)

        swapi_config = SwapiConfig()
        swapi_controller_one.swapi_config = swapi_config 
        self.assertEqual(swapi_config, swapi_controller_one.swapi_config)

