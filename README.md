# SWAPI CLI
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

This is an CLI (Command Line Interface) that which communicates with [Swapi Io](https://swapi.co/).
## About

The language used  in this CLI is [Python3.6](https://docs.python.org/3/index.html), and to build this application was used too [docopt](https://github.com/docopt/docopt) as main library. Being a easy way to everyone reuse or read the code.
#### Libraries used:
- [Docopt](https://github.com/docopt/docopt) - Docopt is Pythonic command line arguments parser
- [Schema](https://pypi.org/project/schema/) - Schema is a library for validating Python data structures.
- [Unittest](https://docs.python.org/3/library/unittest.html) - The unittest unit testing framework.

*Everything else was built using a built-ins modules.*

## Installation

Is required [Python3.6](https://docs.python.org/3/index.html) and [PIP](https://pypi.org/project/pip/) to install the required modules.

Install the modules which is saved in the file **requirements.txt** on the root directory.

```sh
$ pip install -r requirements.txt
```

## Run
When you are using this application, follow these commands to start.
Remember to cofigurate the enviroment and install all the modules.
```sh
$ python main.py
```

## Test
All the CLI program is envolved by unit test to guarantee security and funcionality.
Every code from test is keeped on the **test** folder in the root directory, but you can start
the test task by the **test** file. To do this, just type the follow command:
```sh
$ python test.py
```

## Usage

  > * swapi.py 
  > * swapi.py pilot --name=<name>
  > * swapi.py pilot --fastest 
  > * swapi.py get <object> 
  > * swapi.py get <object> 
  > * swapi.py get <object> (--id=<id>|--search=<text>|--schema)
  > * swapi.py get <object> (--id=<id> --wookiee| --search=<text> --wookiee)
  > * swapi.py (-h | --help)
  > * swapi.py (-v | --version)
      

> This application is CLI (Command Line Interface) to interact with a web API called SWAPI - Star Wars API.
It can be used to search without explicit request to the SWAPI, we build it for you and all you need to do is
ask and see the results ;) 

## Options:

  - --fastest                    | Using this option you can see the faster pilot and his starships.
  - -n <name> --name=<name>     | Use this option so see the max atmosphering speed and starships from the pilot choosen.
  - get <object>                | This command can be used to focus in a specificly object of swapi. It can be 'films', 'people', 'planets', 'species', 'starships' or 'vehicles' 
  - -h --help                   | Show this CLI options in the interface.
  - -v --version                | Show version.
  - -i <id> --id=<id>           | Object's id. Used to find a exactly object in API's search.
  - -s <text> --search=<text>   | Used to filters the set of objects returned.
  - --schema                    | With this option able, it's show a JSON that contains the data structure of <object> choosen.
  - --wookiee                   | This encoding is identical to JSON except with wookieee translations.


## Support
Thank you for considering, contributing to the Swapi io! Rate them [Swapi](https://swapi.co/).

## Contributors

 - Lauro César de Oliveira Teixeira - 0lilauro7@gnail.com
 - LinkedIn - https://www.linkedin.com/in/laurocoliveira/
