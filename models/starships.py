class Starships: 

    def __init__(self):
        self._name = None
        self._model = None
        self._max_speed = None


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        try: 
            if type(value) is str and value.strip() is not '':
                self._name = value.strip()
            else: 
                raise TypeError("The value passed to name property is invalid")
        except Exception as e:
            print(str(e))

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        try: 
            if type(value) is str and value.strip():
                self._model = value.strip()
            else: 
                raise TypeError("The value passed to model property is invalid")
        except Exception as e:
            print(str(e))


    @property
    def max_speed(self):
        return self._max_speed
    
    @max_speed.setter
    def max_speed(self, value):
        try: 
            if (type(value) is int or type(value) is float) and value > -1:
                self._max_speed = value.strip()
            else: 
                raise TypeError("The value passed to max_speed property is invalid")
        except Exception as e:
            print(str(e))