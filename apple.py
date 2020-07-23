import random
from config import Config
# class is used to represent apple as a combined object of X and Y coordinates..


class Apple():

    #When an instance is created, it runs setNewLocation
    def __init__(self):
        self.setNewLocation()
    #sets new location for the apple 
    def setNewLocation(self):

        # This is where the apple is
        self.x = random.randint(0, Config.CELLWIDTH - 1)
        self.y = random.randint(0, Config.CELLHEIGHT - 1)

