import re

class Utils:

    def __init__(self):
        pass
    
    @staticmethod
    def find_speed(text):
        speed = 0
        ocurrencies = re.findall(r"(\d+\.\d+)|(\d+)|(\.\d+)", text.strip.lower)
        if len(ocurrencies) > 0:
            speed = ocurrencies[-1]
        return speed