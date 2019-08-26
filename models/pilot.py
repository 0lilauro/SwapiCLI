class Pilot: 

    def __init__(self):
        self._name = None,
        self.starships = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        try: 
            if type(value) is str and value.strip():
                self._name = value.strip()
            else: 
                raise TypeError("The value passed to name property is invalid")
        except Exception as e:
            print(str(e))