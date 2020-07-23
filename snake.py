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
                        {'x': self.x - 2, 'y': self.y}]

    def update(self, apple):
        if self.sCoords[self.HEAD]['x'] == apple.x and self.sCoords[self.HEAD]['y'] == apple.y:
            apple.setNewLocation()
        else:
            del self.sCoords[-1]  # removes the tail

        if self.direction == self.UP:
            newHead = {'x': self.sCoords[self.HEAD]['x'],
                       'y': self.sCoords[self.HEAD]['y'] - 1}

        elif self.direction == self.RIGHT:
            newHead = {'x': self.sCoords[self.HEAD]['x']+1,
                       'y': self.sCoords[self.HEAD]['y']}

        elif self.direction == self.DOWN:
            newHead = {'x': self.sCoords[self.HEAD]['x'],
                       'y': self.sCoords[self.HEAD]['y'] + 1}

        elif self.direction == self.LEFT:
            newHead = {'x': self.sCoords[self.HEAD]['x']-1,
                       'y': self.sCoords[self.HEAD]['y']}

        self.sCoords.insert(0, newHead)
