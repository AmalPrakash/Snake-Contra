import pygame
import sys
pygame.init()  # initialise all imported pygame modules to get started

# initialise a window for display
DISPLAY = pygame.display.set_mode((800, 600))

# Create a new font object from freesansbold.ttf
BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

# Object helps track time
CLOCK = pygame.time.Clock()

# set a caption for the window
pygame.display.set_caption('SNAKE')

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit

    DISPLAY.fill((0, 0, 0))
    pygame.display.update()
    CLOCK.tick(60)
