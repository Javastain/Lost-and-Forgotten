import pygame

pygame.init()
pygame.mixer.init()
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode((1244, 900), flags)
background = pygame.image.load("Assets/Image Assets/Lost And Forgotten.png").convert_alpha()
background = pygame.transform.scale(background, (1244, 900))
clock = pygame.time.Clock()
running = True


backdrop = pygame.image.load('Assets/Image Assets/Computer Backdrop.png')

screen.fill('#302732')
screen.blit(background, (0, 0))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill('#302732')
    # screen.blit(background, (0, 0))
    # RENDER YOUR GAME HERE

    
    
    # Mouse pointer
    point = pygame.mouse.get_pos()
    # Get mouse button states
    mouse_left, mouse_middle, mouse_right = pygame.mouse.get_pressed()

    # On button
    power_hitbox = pygame.Rect((908,780),(33,33))
    if power_hitbox.collidepoint(point) and mouse_left:
        pygame.mixer.music.load("Assets/Audio Assets/braammmm.wav")
        pygame.mixer.music.play()
        
        pygame.time.delay(2000)
        backdrop.set_alpha(60)
        screen.blit(backdrop,(100,100))
        screen.blit(background, (0, 0))
        pygame.display.flip()

        pygame.time.delay(500)
        backdrop.set_alpha(140)
        screen.blit(backdrop,(100,100))
        screen.blit(background, (0, 0))
        pygame.display.flip()

        pygame.time.delay(300)
        backdrop.set_alpha(255)
        screen.blit(backdrop,(100,100))
        screen.blit(background, (0, 0))
        pygame.display.flip()



    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60



pygame.quit()