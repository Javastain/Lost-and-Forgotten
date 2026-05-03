import pygame
import sys

pygame.init()
pygame.mixer.init()
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode((1244, 900), flags)
pygame.display.set_caption('Eleventh Hour')
outside = pygame.image.load("Assets/Image Assets/Lost And Forgotten.png").convert_alpha()
outside = pygame.transform.scale(outside, (1244, 900))
clock = pygame.time.Clock()
running = True


backdrop = pygame.image.load('Assets/Image Assets/Computer Backdrop.png')
login_screen = pygame.image.load('Assets/Image Assets/Login Screen.png')

power_hitbox = pygame.Rect((908,780),(33,33))
nicole_hitbox = pygame.Rect((305,260),(200,70))
michael_hitbox = pygame.Rect((305,360),(200,70))
john_hitbox = pygame.Rect((305,460),(200,70))
marion_hitbox = pygame.Rect((305,560),(200,70))

computer_on = False
account = "no one"
account_selected = "no one"
mail_open = False
notes_open = False
photos_open = False

password_input = ""
password_active = False
password_color_active = pygame.Color((255,255,255))
password_color_passive = pygame.Color((240,240,240))
password_color = password_color_passive

screen.fill('#302732')
screen.blit(outside, (0, 0))

header = pygame.font.SysFont('tahoma', 25)
body_text = pygame.font.SysFont('tahoma', 12)

login_prompt = header.render('To begin, click on your profile', True, (255, 255, 255))
login_prompt_rect = login_prompt.get_rect()
login_prompt_rect.center = (740, 550)
password_input_rect = pygame.Rect((625, 540), (250, 30))


# This would draw a rectangle that perfectly fits over the screen. Just so we know its dimensions.
# pygame.draw.rect(screen, "white", pygame.Rect(622,450,0,0).inflate(690,570))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # fill the screen with a color to wipe away anything from last frame

        # RENDER YOUR GAME HERE

        
        
        # Mouse pointer
        point = pygame.mouse.get_pos()
        # Get mouse button states
        mouse_left, mouse_middle, mouse_right = pygame.mouse.get_pressed()

        # On button
        if power_hitbox.collidepoint(point) and mouse_left:
            pygame.mixer.music.load("Assets/Audio Assets/braammmm.wav")
            pygame.mixer.music.play()
            
            pygame.time.delay(1600)
            login_screen.set_alpha(60)
            screen.blit(login_screen,(276,165))
            screen.blit(outside, (0, 0))
            pygame.display.flip()

            pygame.time.delay(300)
            login_screen.set_alpha(140)
            screen.blit(login_screen,(276,165))
            screen.blit(outside, (0, 0))
            pygame.display.flip()

            pygame.time.delay(150)
            login_screen.set_alpha(255)
            screen.blit(login_screen,(276,165))
            screen.blit(outside, (0, 0))
            pygame.display.flip()

            power_hitbox = pygame.Rect((0,0),(0,0))

            computer_on = True


        if computer_on == True and account == "no one" and account_selected == "no one":
            screen.blit(login_prompt, login_prompt_rect)
            
            
            if event.type == pygame.MOUSEBUTTONDOWN and nicole_hitbox.collidepoint(point):
                account_selected = "nicole"
            if event.type == pygame.MOUSEBUTTONDOWN and michael_hitbox.collidepoint(point):
                account_selected = "michael"
            if event.type == pygame.MOUSEBUTTONDOWN and john_hitbox.collidepoint(point):
                account_selected = "john"
            if event.type == pygame.MOUSEBUTTONDOWN and marion_hitbox.collidepoint(point):    
                account_selected = "marion"

        if account_selected != "no one":
            pygame.draw.rect(screen, (103,133,206), ((277+290,165+320),(350,207)))            
            if event.type == pygame.MOUSEBUTTONDOWN and password_input_rect.collidepoint(point):
                password_active = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    password_input = password_input[:-1]
                    text = body_text.render(password_input, True, (255, 255, 255))
                if event.key == pygame.K_RETURN:
                    print(password_input) 
            if event.type == pygame.TEXTINPUT:
                password_input += event.text

            """
            # if the key is physically pressed down
            if event.type == pygame.TEXTINPUT:
                if event.text == pygame.K_BACKSPACE:
                    # stores text except last letter
                    password_input = password_input[0:-1]
                else:
                    pygame.key.set_repeat(1000,500)
                    password_input += event.text
            """

            if password_active:
                password_color = password_color_active
            else:
                password_color = password_color_passive
        
            pygame.draw.rect(screen, password_color, password_input_rect)

            # Renders the text
            password = body_text.render(password_input, True, (0, 0, 0))
            screen.blit(password, (password_input_rect.x + 5, password_input_rect.y + 5))
            password_input_rect.w = max(100, password.get_width() + 10)
            
    # pygame.draw.rect(screen, "white", (287,655,70,70))
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60



pygame.quit()