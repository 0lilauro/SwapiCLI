import unittest

class VerifyDependences(unittest.TestCase):
    def import_all_modules(self):
        erros = False
        try: 
            import re
            import docopt
            import schema
            from models.swapi_config import SwapiConfig
            from controllers.swapi_controller import SwapiController
            import utils.swapi_error
            from utils.utils import Utils
            from services.swapi_service import SwapiService
            from models.pilot import Pilot
            from models.starships import Starships 
            from models.swapi_config import SwapiConfig 
            from controllers.swapi_controller import SwapiController 
        except:
            erros = True
        
        self.assertFalse(erros)