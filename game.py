from config import Config
from snake import Snake
from apple import Apple
import pygame
import sys

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Snake')
        self.apple = Apple()
        self.snake = Snake()

    def drawGrid(self):

        # vertical lines
        for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.DARKGRAY,
                             (x, 0), (x, Config.WINDOW_HEIGHT))
        # horizontal lines
        for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.DARKGRAY,
                             (0, y), (Config.WINDOW_WIDTH, y))

    def draw(self):
        self.screen.fill(Config.BG_COLOR)
        self.drawGrid()
        pygame.display.update()
        self.clock.tick(Config.FPS)

    def handleKeyEvents(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()

    def run(self):
        # Main game loop
        #self.showStartScreen()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyEvents(event)
                    # if event.key == pygame.K_ESCAPE:
                    # pygame.quit()
                    # sys.exit

            #self.snake.update(self.apple)
            self.draw()
            #if self.isGameOver():
               # break
