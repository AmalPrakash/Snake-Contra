from config import Config
import random
class Snake():
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    HEAD = 0
    
    def __init__(self):
        # Starting coordinates --> 5 cells away from x and y
        self.x = random.randint(5, Config.CELLWIDTH - 6)
        self.y = random.randint(5, Config.CELLHEIGHT - 6)

        # Move right
        self.direction = self.RIGHT

        # This is the snake
        self.sCoords = [{'x': self.x, 'y': self.y},
                        {'x': self.x - 1, 'y': self.y},
                        {'x':self.x-2,'y':self.y}]
        