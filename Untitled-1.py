# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode((1244, 900), flags)
background = pygame.image.load("Assets/Image Assets/Lost And Forgotten.png").convert_alpha()
background = pygame.transform.scale(background, (1244, 900))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()