class SwapiConfig():

  def __init__(self):
    self._get = None
    self._object_swapi = None
    self._schema = None
    self._wookiee = None
    self._id = None
    self._help = None
    self._version = None
    self._search = None
    self._name = None
    self._fastest = None
    self._pilot = None

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
  def wookiee(self):
    return self._wookiee
  
  @wookiee.setter
  def wookiee(self, value):
    try: 
      if type(value) is bool:
        self._wookiee = value
      else: 
        raise TypeError("The value passed to wookiee property is invalid")
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
      if value is None or type(value) is int or type(value) is str:
        if value is not None and int(value) > 0:
          self._id = int(value)
        elif value is None:
          self._id = None
        else: 
          raise ValueError("The value of id must be an interger greater than 0")
      else: 
        print(type(value))
        raise TypeError("The value passed to id property is invalid")
    except Exception as e:
      print(str(e))
      
  @property
  def search(self):
    return self._search
  
  @search.setter
  def search(self, value):
    try: 
      if type(value) is str and value.strip:
        self._search = value
      elif value is None:
        self._search = None
      else: 
        raise TypeError("The value passed to search property is invalid")
    except Exception as e:
      print(str(e))

  @property
  def pilot(self):
    return self._pilot
  
  @pilot.setter
  def pilot(self, value):
    try: 
      if type(value) is bool:
        self._pilot = value
      else: 
        raise TypeError("The value passed to pilot property is invalid")
    except Exception as e:
      print(str(e))

  @property
  def fastest(self):
    return self._fastest
  
  @fastest.setter
  def fastest(self, value):
    try: 
      if type(value) is bool:
        self._fastest = value
      else: 
        raise TypeError("The value passed to fastest property is invalid")
    except Exception as e:
      print(str(e))

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, value):
    try: 
      if type(value) is str and value.strip:
        self._name = value
      elif value is None:
        self._name = None
      else: 
        raise TypeError("The value passed to name property is invalid")
    except Exception as e:
      print(str(e))

  def read_arguments(self, arguments):
    try: 
      self.get = arguments['get']
      self.object_swapi = arguments['<object>']
      self.schema = arguments['--schema']
      self.wookiee = arguments['--wookiee']
      self.id = arguments['--id']
      self.search = arguments['--search']
      self.help = arguments['--help']
      self.version = arguments['--version']
      self.fastest = arguments['--fastest']
      self.name = arguments['--name']
      self.pilot = arguments['pilot']
    except Exception as e:
      print(str(e))
