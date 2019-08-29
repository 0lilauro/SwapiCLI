import re
from pprint import pprint
from models.pilot import Pilot
from models.starships import Starships

class Utils:

    def __init__(self):
        pass
    
    @staticmethod
    def find_speed(text):
        speed = 0
        ocurrencies = list(re.findall(r"\d+", text.strip().lower()))
        if len(ocurrencies) > 0:
            speed = ocurrencies[-1]
        return int(speed)

    @staticmethod
    def print_one(pilot, fastest = False):
        name = "The fastest pilot" if fastest else "Pilot name"
        ship = "The fastest starship" if fastest else "Naves"
        naves_print = ""
        for starship in pilot.starships:
            naves_print += "\tName: {}\n\tModel: {}\n\tMax atmosphering speed: {}\n\n".format(
                starship.name,
                starship.model,
                starship.max_speed,
            )
        text_print = """\n------------------------------------------------------\n{}:\n\t{}\n\n{}:\n{}""".format(
                name,
                pilot.name,
                ship,
                naves_print
            )
        print(text_print)

    
    @staticmethod
    def find_max_speed(list_pilots):
        starship = Starships() 
        starship.max_speed = 0
        pilot = Pilot()
        for each_pilot in list_pilots: 
            for each_starship in each_pilot.starships:
                if each_starship.max_speed > starship.max_speed:
                    starship = each_starship
                    pilot = each_pilot
                else:
                    continue
        pilot.starships = [starship]
        return pilot
                

