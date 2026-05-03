import pygame

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

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('#302732')
    screen.blit(background, (0, 0))
    # RENDER YOUR GAME HERE

    
    
    # Mouse pointer
    point = pygame.mouse.get_pos()

    # On button
    power_hitbox = pygame.Rect((1000,800),(1050,850))
    pygame.draw.rect(screen, '#FFFFFF', power_hitbox)


    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60



pygame.quit()