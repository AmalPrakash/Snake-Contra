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
        pygame.display.set_caption('SNAKE')
        self.apple = Apple()
        self.snake = Snake()

    def drawGrid(self):
        for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):  # draw vertical lines
            pygame.draw.line(self.screen, Config.BG_COLOR,
                             (x, 0), (x, Config.WINDOW_HEIGHT))

        for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):  # draw horizontal lines
            pygame.draw.line(self.screen, Config.BG_COLOR,
                             (0, y), (Config.WINDOW_WIDTH, y))

    def drawSnake(self):
        for coord in self.snake.sCoords:
            x = coord['x'] * Config.CELLSIZE
            y = coord['y'] * Config.CELLSIZE
            snakeSegmentRect = pygame.Rect(
                x, y, Config.CELLSIZE, Config.CELLSIZE)
            pygame.draw.rect(self.screen, Config.DARKGREEN, snakeSegmentRect)
            snakeInnerSegmentRect = pygame.Rect(
                x + 4, y + 4, Config.CELLSIZE - 8, Config.CELLSIZE - 8)
            pygame.draw.rect(self.screen, Config.GREEN, snakeInnerSegmentRect)

    def drawApple(self):
        x = self.apple.x * Config.CELLSIZE
        y = self.apple.y * Config.CELLSIZE
        appleRect = pygame.Rect(
            x, y, Config.CELLSIZE, Config.CELLSIZE)
        pygame.draw.rect(self.screen, Config.RED, appleRect)

    def drawScore(self, score):
        scoreSurf = self.BASICFONT.render(
            'Score: %s' % (score), True, Config.WHITE)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (Config.WINDOW_WIDTH - 120, 10)
        self.screen.blit(scoreSurf, scoreRect)

    def draw(self):
        self.screen.fill(Config.BG_COLOR)
        self.drawGrid()
        self.drawSnake()
        self.drawApple()
        self.drawScore(len(self.snake.sCoords) - 3)
        pygame.display.update()
        self.clock.tick(Config.FPS)

    def checkForKeyPress(self):
        if len(pygame.event.get(pygame.QUIT)) > 0:
            pygame.quit()

        keyUpEvents = pygame.event.get(pygame.KEYUP)

        if len(keyUpEvents) == 0:
            return None

        if keyUpEvents[0].key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

        return keyUpEvents[0].key

    def handleKeyEvents(self, event):
        if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.snake.direction != self.snake.RIGHT:
            self.snake.direction = self.snake.RIGHT
        elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.snake.direction != self.snake.LEFT:
            self.snake.direction = self.snake.LEFT
        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.snake.direction != self.snake.DOWN:
            self.snake.direction = self.snake.DOWN
        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.snake.direction != self.snake.UP:
            self.snake.direction = self.snake.UP
        elif event.key == pygame.K_ESCAPE:
            pygame.quit()

    def resetGame(self):
        del self.snake
        del self.apple
        self.snake = Snake()
        self.apple = Apple()

        return True

    def isGameOver(self):
        if (self.snake.sCoords[self.snake.HEAD]['x'] == -1 or
            self.snake.sCoords[self.snake.HEAD]['x'] == Config.CELLWIDTH or
            self.snake.sCoords[self.snake.HEAD]['y'] == -1 or
                self.snake.sCoords[self.snake.HEAD]['y'] == Config.CELLHEIGHT):
            return self.resetGame()

        for sBody in self.snake.sCoords[1:]:
            if sBody['x'] == self.snake.sCoords[self.snake.HEAD]['x'] and sBody['y'] == self.snake.sCoords[self.snake.HEAD]['y']:
                return self.resetGame()

    def displayGameOver(self):
        gameFont = pygame.font.SysFont('bradleyhanditc', 40)
        overFont = pygame.font.SysFont('bradleyhanditc', 160)
        gameSurf = gameFont.render('Game', True, Config.WHITE)
        overSurf = overFont.render('Over', True, Config.WHITE)
        gameRect = gameSurf.get_rect()
        overRect = overSurf.get_rect()
        gameRect.midtop = (Config.WINDOW_WIDTH / 2, 120)
        overRect.midtop = (Config.WINDOW_WIDTH / 2, gameRect.height + 60)
        self.screen.blit(gameSurf, gameRect)
        self.screen.blit(overSurf, overRect)
        pygame.display.update()
        pygame.time.wait(500)

        self.checkForKeyPress()  # clear out any key presses in the event queue
        while True:
            if self.checkForKeyPress():
                pygame.event.get()  # clear event queue
                return

    def creditshow(self):
        pressKeySurf = self.BASICFONT.render(
            'An AmalPrakash adaptation of the classic Snake Xenzia.', True, Config.DARKGRAY2)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (Config.WINDOW_WIDTH - 600,
                                Config.WINDOW_HEIGHT - 30)
        self.screen.blit(pressKeySurf, pressKeyRect)

    def drawPressKeyMsg(self):
        pressKeySurf = self.BASICFONT.render(
            'Press any key to start', True, Config.DARKGRAY)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (Config.WINDOW_WIDTH - 400,
                                Config.WINDOW_HEIGHT - 30)
        self.screen.blit(pressKeySurf, pressKeyRect)

    def showStartScreen(self):

        titleFont = pygame.font.SysFont(
            'bradleyhanditc', 75)
        instSurf1 = titleFont.render('UPs are DOWNs', True, Config.WHITE)
        instSurf2 = titleFont.render('LEFTs are RIGHTs', True, Config.WHITE)
        instRect1 = instSurf1.get_rect()
        instRect2 = instSurf2.get_rect()
        instRect1.midtop = (Config.WINDOW_WIDTH / 2, 100)
        instRect2.midtop = (Config.WINDOW_WIDTH / 2, instRect1.height + 100)
        self.screen.blit(instSurf1, instRect1)
        self.screen.blit(instSurf2, instRect2)

        self.creditshow()
        pygame.display.update()
        pygame.time.wait(2845)

        titleSurf = titleFont.render(
            'SNAKE CONTRA!', True, Config.WHITE, Config.BG_COLOR)
        
            #scene contra
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return
            self.screen.fill(Config.BG_COLOR)
            Rect = titleSurf.get_rect()
            Rect.center = (Config.WINDOW_WIDTH / 2,
                           Config.WINDOW_HEIGHT / 2)
            self.screen.blit(titleSurf, Rect)
            self.drawPressKeyMsg()
            pygame.display.update()
            self.clock.tick(Config.MENU_FPS)

    def run(self):
        self.showStartScreen()

        while True:
            self.gameLoop()
            self.displayGameOver()

    def gameLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyEvents(event)

            self.snake.update(self.apple)
            self.draw()
            if self.isGameOver():
                break
