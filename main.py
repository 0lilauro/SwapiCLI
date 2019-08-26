"""Swapi CLI 1.0

Usage:
  swapi.py 
  swapi.py get <object> 
  swapi.py get <object> (--id=<id>|--search=<text>|--schema)
  swapi.py get <object> (--id=<id> --wookiee| --search=<text> --wookiee)
  swapi.py (-h | --help)
  swapi.py (-v | --version)

This application is CLI (Command Line Interface) to interact with a web API called SWAPI - Star Wars API.
It can be used to search without explicit request to the SWAPI, we build it for you and all you need to do is
ask and see the results ;) 

Options:

  get <object>                This command can be used to focus in a specificly object of swapi. \n It can be 'films', 'people', 'planets', 'species', 'starships' or 'vehicles' 
  -h --help                   Show this CLI options in the interface.
  -v --version                Show version.
  -i <id> --id=<id>           Object's id. Used to find a exactly object in API's search.
  -s <text> --search=<text>   Used to filters the set of objects returned.
  --schema                    With this option able, it's show a JSON that contains the data structure of <object> choosen.
  --wookiee                   This encoding is identical to JSON except with wookieee translations.

"""

from docopt import docopt
from schema import Schema, And, Or, Use, SchemaError
import swapi_error
from models.swapi_config import SwapiConfig
from controller.swapi_controller import SwapiController

if __name__ == '__main__':
  arguments = docopt(__doc__, version='Swapi CLI 1.0')
  
  if not any(list(arguments.values())):
    exit(__doc__)
  
  schema = Schema({
    'get': Or(True, False, error=swapi_error.get),
    '<object>': Or(None, And(Use(str), lambda obj: obj in ('films', 'people', 'planets', 'species', 'starships', 'vehicles'),
        error=swapi_error.swapi_object
    )),
    '--schema': Or(True, False, error=swapi_error.schema),
    '--wookiee': Or(True, False, error=swapi_error.wookiee),
    '--id': Or(None, And(Use(int), lambda n: n > 0, error=swapi_error.id)),
    '--search': Or(None, And(Use(str), lambda n: n.strip(), error=swapi_error.search)),
    '--help': Or(True, False, error=swapi_error.help),
    '--version': Or(True, False, error=swapi_error.version),
  })
  
  # 'FILE': [Use(open, error='FILE should be readable')],
  # 'PATH': And(os.path.exists, error='PATH should exist'),
  
  try:
    # print(arguments)
    args = schema.validate(arguments)
    swapi_config = SwapiConfig()
    swapi_config.read_arguments(arguments)
    swapi_controller = SwapiController(swapi_config)
  except SchemaError as e:
    exit(e)

