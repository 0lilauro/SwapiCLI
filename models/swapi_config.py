class SwapiConfig():

  def __init__(self):
    self._get = None
    self._object_swapi = None
    self._schema = None
    self._wookie = None
    self._id = None
    self._help = None
    self._version = None

  @property
  def get(self):
    return self._get
  
  @get.setter
  def get(self, value):
    try: 
      if type(value) is bool:
        self._get = value
      else: 
        raise TypeError("The value passed to get property is invalid")
    except Exception as e:
      print(str(e))

  @property
  def object_swapi(self):
    return self._object_swapi
  
  @object_swapi.setter
  def object_swapi(self, value):
    try: 
      if (value is None) or type(value) is str:
        if value in ('films', 'people', 'planets', 'species', 'starships', 'vehicles'):
          self._object_swapi = value
        else: 
          raise ValueError("The value of Object swapi must be 'films', 'people', 'planets', 'species', 'starships' or 'vehicles'")
      else: 
        raise TypeError("The value passed to swapi object property is invalid")
    except Exception as e:
      print(str(e))

  @property
  def schema(self):
    return self._schema

  @schema.setter
  def schema(self, value):
    try: 
      if type(value) is bool:
        self._schema = value
      else: 
        raise TypeError("The value passed to schema property is invalid")
    except Exception as e:
      print(str(e))

  @property
  def wookie(self):
    return self._wookie
  
  @wookie.setter
  def wookie(self, value):
    try: 
      if type(value) is bool:
        self._wookie = value
      else: 
        raise TypeError("The value passed to wookie property is invalid")
    except Exception as e:
      print(str(e))

  @property
  def help(self):
    return self._help
  
  @help.setter
  def help(self, value):
    try: 
      if type(value) is bool:
        self._help = value
      else: 
        raise TypeError("The value passed to help property is invalid")
    except Exception as e:
      print(str(e))

  @property
  def version(self):
    return self._version
  
  @version.setter
  def version(self, value):
    try: 
      if type(value) is bool:
        self._version = value
      else: 
        raise TypeError("The value passed to version property is invalid")
    except Exception as e:
      print(str(e))

  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, value):
    try: 
      if (value is None) or type(value) is int or type(value) is str:
        if int(value) > 0:
          self._id = value
        else: 
          raise ValueError("The value of id must be an interger greater than 0")
      else: 
        print(type(value))
        raise TypeError("The value passed to id property is invalid")
    except Exception as e:
      print(str(e))

  def read_arguments(self, arguments):
    try: 
      self.get = arguments['get']
      self.object_swapi = arguments['<object>']
      self.schema = arguments['--schema']
      self.wookie = arguments['--wookie']
      self.id = int(arguments['--id'])
      self.help = arguments['--help']
      self.version = arguments['--version']
    except Exception as e:
      print(str(e))