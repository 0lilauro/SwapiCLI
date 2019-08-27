import unittest
from controllers.swapi_controller import SwapiController
from models.swapi_config import SwapiConfig
from models.starships import Starships
from models.pilot import Pilot

class VerifySwapiConfig(unittest.TestCase):
    def test_instance_property(self):
        swapi_config = SwapiConfig()
        self.assertEqual(None, swapi_config.get)
        self.assertEqual(None, swapi_config.object_swapi)
        self.assertEqual(None, swapi_config.schema)
        self.assertEqual(None, swapi_config.wookiee)
        self.assertEqual(None, swapi_config.id)
        self.assertEqual(None, swapi_config.help)
        self.assertEqual(None, swapi_config.version)
        self.assertEqual(None, swapi_config.search)
        self.assertEqual(None, swapi_config.name)
        self.assertEqual(None, swapi_config.fastest)
        self.assertEqual(None, swapi_config.pilot)

    def test_instance_values_correct(self):
        arguments = {}
        arguments['get'] = True
        arguments['<object>'] = "people"
        arguments['--schema'] = True
        arguments['--wookiee'] = True
        arguments['--id'] = 2
        arguments['--search'] = True
        arguments['--help'] = True
        arguments['--version'] = True
        arguments['--fastest'] = "test user"
        arguments['--name'] = True
        arguments['pilot'] = "test user"

        swapi_config = SwapiConfig()
        swapi_config.read_arguments(arguments)

        self.assertEqual(arguments['get'], swapi_config.get)
        self.assertEqual(arguments['<object>'], swapi_config.object_swapi)
        self.assertEqual(arguments['--schema'], swapi_config.schema)
        self.assertEqual(arguments['--wookiee'], swapi_config.wookiee)
        self.assertEqual(arguments['--id'], swapi_config.id)
        self.assertEqual(arguments['--search'], swapi_config.search)
        self.assertEqual(arguments['--help'], swapi_config.help)
        self.assertEqual(arguments['--version'], swapi_config.version)
        self.assertEqual(arguments['--fastest'], swapi_config.fastest)
        self.assertEqual(arguments['--name'], swapi_config.name)
        self.assertEqual(arguments['pilot'], swapi_config.pilot)

class VerifyStarship(unittest.TestCase):
    def test_instance_property(self):
        starship = Starships()
        self.assertEqual(None, starship.name)
        self.assertEqual(None, starship.model)
        self.assertEqual(None, starship.max_speed)

    def test_instance_values_correct(self):
        starship = Starships()

        nome = "DEATH STAR"
        model = "DEATH STAR"
        max_speed = 1231

        starship.name = nome
        starship.model = model
        starship.max_speed = max_speed

        self.assertEqual(nome, starship.name)
        self.assertEqual(model, starship.model)
        self.assertEqual(max_speed, starship.max_speed)

class VerifyPilot(unittest.TestCase):
    def test_instance_property(self):
        pilot = Pilot()
        self.assertEqual(None, pilot.name)
        self.assertEqual([], pilot.starships)

    def test_instance_values_correct(self):
        pilot = Pilot()
        ships = [1,2,3]
        name = "John Sena"

        pilot.name = name
        pilot.starships.append(1)
        pilot.starships.append(2)
        pilot.starships.append(3)
        
        self.assertEqual(name, pilot.name)
        self.assertEqual(ships, pilot.starships)

