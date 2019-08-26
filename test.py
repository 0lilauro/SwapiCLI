from services.swapi_service import SwapiService
from pprint import pprint

swapi_service = SwapiService()

# endpoint = swapi_service.build_find_url('people')
endpoint = swapi_service.build_schema_url('people')
params = swapi_service.build_params(False)

print(endpoint)
pprint(endpoint)
response = swapi_service.make_request(endpoint, params)
pprint(response.status_code)
pprint(response.json())

