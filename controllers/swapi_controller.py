from pprint import pprint
from utils.utils import Utils
from services.swapi_service import SwapiService
from models.swapi_config import SwapiConfig
from models.pilot import Pilot
from models.starships import Starships

class SwapiController:
    
    def __init__(self, swapi_config = None):
        self._swapi_config = None
        if swapi_config is not None:
            self._swapi_config = swapi_config
        
    @property
    def swapi_config(self):
        return self._swapi_config
  
    @swapi_config.setter
    def swapi_config(self, value):
        try: 
            if isinstance(value, SwapiConfig):
                self.swapi_config = value
            elif value is None:
                pass
            else: 
                raise TypeError("The value passed to SwapiConfig property is not a SwapiModel instance")
        except Exception as e:
            print(str(e))
    
    def run(self): 
        if self._swapi_config.help or self._swapi_config.version:
            return None
        elif self._swapi_config.get:
            return self.get_command()
        elif self._swapi_config.pilot:
            return self.pilot_command()
        else:
            print('Please use a valid command. Type "python main.py" to see the options and usage !')
            return {}
            
    def get_command(self): 
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
        try: 
            response = swapi_service.make_request(
                endpoint,
                params
            )
            result = response.json()
        except:
            print("An error has been occurred in the attemp to convert the search to JSON") 
        finally: 
            return result

    def pilot_command(self):
        final_response = None
        pilots = []
        result = {}
        swapi_service = SwapiService()

        if self.swapi_config.name and self.swapi_config.name.strip():
            endpoint = swapi_service.build_find_url(
                'people'
            )
            params = swapi_service.build_params(
                None,
                self.swapi_config.name.strip().lower()
            )
            result = {}
            try: 
                response = swapi_service.make_request(
                    endpoint,
                    params
                )
                result = response.json()
            except:
                print("An error has been occurred in the attemp to convert the search to JSON")
            
            if "results" in result:
                pilotOne = self.fill_pilot(result[0])
                if pilotOne is not None:
                    pprint(pilotOne)
                else: 
                    print("No pilot with the typed name was found.")
            else: 
                print("No pilot with the typed name was found.")

        elif self.swapi_config.fastest:
            next_page = swapi_service.build_find_url(
                'people'
            )
            while next_page:
                result = {}
                try:
                    response = swapi_service.simple_request(next_page)
                    if response.status_code == 200:
                        result = response.json()
                except Exception:
                    print("An error has been occurred in the attemp to convert the search to JSON") 
                finally:
                    if result and 'results' in result:
                        for pilot in result['results']:
                            filled_pilot = self.fill_pilot(pilot)
                            if filled_pilot is not None: 
                                pilots.append(filled_pilot)
                if result and 'next' in result:
                    next_page = result['next']
            
            pprint(pilots)

    def fill_starship(self, endpoint):
        starship = Starships()
        swapi_service = SwapiService()
        result = {}
        try:
            response = swapi_service.simple_request(endpoint)
            if response.status_code == 200:
                result = response.json()
        except Exception:
            print("An error has been occurred in the attemp to convert the search to JSON") 
        
        if result:
            if 'name' in result:
                starship.name = str(result['name']).upper() 
            if 'model' in result:
                starship.model = str(result['model']).upper() 
            if 'max_atmosphering_speed' in result:
                starship.max_speed = Utils.find_speed(result['model']) 
            return starship
        else:
            return None

    def fill_pilot(self, pilot_response):
        pilot = Pilot()
        if 'name' in pilot_response: 
            pilot.name = pilot_response['name']
        if 'starships' in pilot_response:
            for starship in pilot_response['starships']:
                starship_response = self.fill_starship(starship)
                if starship_response is not None:
                    pilot.starships.append(starship_response)
        else:
            pilot = None
        return pilot