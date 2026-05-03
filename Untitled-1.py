import pygame
import datetime

pygame.init()
pygame.mixer.init()
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode((1244, 900), flags)
pygame.display.set_caption("Eleventh Hour")
clock = pygame.time.Clock()
running = True

backdrop = pygame.image.load(
    "Assets/Image Assets/Computer Backdrop.png"
).convert_alpha()
login_screen = pygame.image.load("Assets/Image Assets/Login Screen.png").convert_alpha()
nicole_pfp = pygame.image.load("Assets/Image Assets/Nicole pfp.png").convert_alpha()
michael_pfp = pygame.image.load("Assets/Image Assets/Michael pfp.png").convert_alpha()
john_pfp = pygame.image.load("Assets/Image Assets/John pfp.png").convert_alpha()
marion_pfp = pygame.image.load("Assets/Image Assets/Marion pfp.png").convert_alpha()
outside = pygame.image.load(
    "Assets/Image Assets/Lost And Forgotten.png"
).convert_alpha()
mail_UI = pygame.image.load("Assets/Image Assets/Email UI.png").convert_alpha()
music_paused_UI = pygame.image.load("Assets/Image Assets/Music UI.png").convert_alpha()
music_playing_UI = pygame.image.load(
    "Assets/Image Assets/Music UI (playing).png"
).convert_alpha()
notes_UI = pygame.image.load("Assets/Image Assets/Notes UI.png").convert_alpha()
photos_UI = pygame.image.load("Assets/Image Assets/Photos UI.png").convert_alpha()
logout_icon = pygame.image.load("Assets/Image Assets/Exit Icon.png").convert_alpha()
mail_icon = pygame.image.load("Assets/Image Assets/Mail Icon.png").convert_alpha()
music_icon = pygame.image.load("Assets/Image Assets/Music Icon.png").convert_alpha()
notes_icon = pygame.image.load("Assets/Image Assets/Notes Icon.png").convert_alpha()
photos_icon = pygame.image.load("Assets/Image Assets/Photos Icon.png").convert_alpha()
mail_icon = pygame.transform.scale(mail_icon, (75, 95))
music_icon = pygame.transform.scale(music_icon, (75, 95))
notes_icon = pygame.transform.scale(notes_icon, (75, 95))
photos_icon = pygame.transform.scale(photos_icon, (75, 95))

outside = pygame.transform.scale(outside, (1244, 900))

power_hitbox = pygame.Rect((908, 780), (33, 33))
nicole_hitbox = pygame.Rect((305, 260), (200, 70))
michael_hitbox = pygame.Rect((305, 360), (200, 70))
john_hitbox = pygame.Rect((305, 460), (200, 70))
marion_hitbox = pygame.Rect((305, 560), (200, 70))
logout_hitbox = pygame.Rect((285, 665), (60, 60))
UI_Exit_hitbox = pygame.Rect((400, 665), (60, 60))
mail_icon_hitbox = pygame.Rect((0, 0), (0, 0))
music_icon_hitbox = pygame.Rect((0, 0), (0, 0))
notes_icon_hitbox = pygame.Rect((0, 0), (0, 0))
photos_icon_hitbox = pygame.Rect((0, 0), (0, 0))

computer_on = False
account = "no one"
account_selected = "no one"
music_open = False
mail_open = False
notes_open = False
photos_open = False
hint = False

password_input = ""
password_active = False
password_color_active = pygame.Color((255, 255, 255))
password_color_passive = pygame.Color((200, 200, 200))
password_color = password_color_passive

screen.fill("#302732")
screen.blit(outside, (0, 0))

header = pygame.font.SysFont("tahoma", 25)
body_text = pygame.font.SysFont("tahoma", 12)


login_prompt = header.render("To begin, click on your profile", True, (255, 255, 255))
login_prompt_rect = login_prompt.get_rect()
login_prompt_rect.center = (740, 550)

password_prompt = body_text.render("Password:", True, (255, 255, 255))
password_prompt_rect = password_prompt.get_rect()
password_prompt_rect.center = (650, 525)

hint_prompt = body_text.render("Need a hint?", True, (255, 255, 255))
hint_prompt_rect = password_prompt.get_rect()
hint_prompt_rect.center = (650, 585)

password_input_rect = pygame.Rect((625, 540), (250, 30))

current_time = datetime.datetime.now()
init_second = int(current_time.strftime("%S"))
init_minute = int(current_time.strftime("%M"))
init_hour = int(current_time.strftime("%I"))
init_meridian = current_time.strftime("%p")

second = (60 + int(current_time.strftime("%S")) - init_second) % 60
minute = 3 + ((60 + int(current_time.strftime("%M")) - init_minute) % 60)
hour = 11 + ((12 + int(current_time.strftime("%I")) - init_hour) % 12)
meridian = current_time.strftime("%p")

clock_display = body_text.render(
    "December 31, 1999, AAAAAAAAAAAAAAAA "
    + str(hour)
    + ":"
    + str(minute)
    + ":"
    + str(second)
    + " "
    + meridian,
    True,
    (0, 0, 0),
)
clock_display_rect = clock_display.get_rect()
clock_display_rect.center = (740, 715)


# This would draw a rectangle that perfectly fits over the screen. Just so we know its dimensions.
# pygame.draw.rect(screen, "white", pygame.Rect(622,450,0,0).inflate(690,570))
# pygame.draw.rect(screen, "white", pygame.Rect(277,165,690,570)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
            screen.blit(login_screen, (276, 165))
            screen.blit(outside, (0, 0))
            pygame.display.flip()

            pygame.time.delay(300)
            login_screen.set_alpha(140)
            screen.blit(login_screen, (276, 165))
            screen.blit(outside, (0, 0))
            pygame.display.flip()

            pygame.time.delay(150)
            login_screen.set_alpha(255)
            screen.blit(login_screen, (276, 165))
            screen.blit(outside, (0, 0))
            pygame.display.flip()

            power_hitbox = pygame.Rect((0, 0), (0, 0))

            computer_on = True

        if computer_on == True and account == "no one":
            screen.blit(login_prompt, login_prompt_rect)

            if event.type == pygame.MOUSEBUTTONDOWN and nicole_hitbox.collidepoint(
                point
            ):
                account_selected = "nicole"
                screen.blit(nicole_pfp, (710, 300))
            if event.type == pygame.MOUSEBUTTONDOWN and michael_hitbox.collidepoint(
                point
            ):
                account_selected = "michael"
                screen.blit(michael_pfp, (710, 300))
            if event.type == pygame.MOUSEBUTTONDOWN and john_hitbox.collidepoint(point):
                account_selected = "john"
                screen.blit(john_pfp, (710, 300))
            if event.type == pygame.MOUSEBUTTONDOWN and marion_hitbox.collidepoint(
                point
            ):
                account_selected = "marion"
                screen.blit(marion_pfp, (710, 300))

        if account == "no one" and account_selected != "no one":
            pygame.draw.rect(
                screen, (103, 133, 206), ((277 + 290, 165 + 320), (350, 207))
            )

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and password_input_rect.collidepoint(point)
            ):
                password_active = True

            if event.type == pygame.KEYDOWN and password_active == True:
                if event.key == pygame.K_BACKSPACE:
                    password_input = password_input[:-1]
                    text = body_text.render(password_input, True, (255, 255, 255))
                if event.key == pygame.K_RETURN:
                    password_active = False

                    if account_selected == "nicole":
                        account = "nicole"
                    if (
                        account_selected == "michael"
                        and password_input == "kegsmasher1999"
                    ):
                        account = "michael"
                    if account_selected == "john" and password_input == "M00nlander":
                        account = "john"
                    if account_selected == "marion" and password_input == "I, Mudd":
                        account = "marion"

                    if account != "no one":
                        pygame.time.delay(900)
                        screen.blit(backdrop, (276, 165))

                        # Clock bar
                        pygame.draw.rect(screen, (230, 235, 240), (277, 700, 690, 35))
                        screen.blit(clock_display, clock_display_rect)

                        if account == "nicole":
                            screen.blit(music_icon, (498, 320))
                            music_icon_hitbox = pygame.Rect((498, 320), (75, 95))
                            screen.blit(notes_icon, (648, 320))
                            notes_icon_hitbox = pygame.Rect((648, 320), (75, 95))
                            screen.blit(photos_icon, (498, 470))
                            photos_icon_hitbox = pygame.Rect((498, 470), (75, 95))
                            screen.blit(mail_icon, (648, 470))
                            mail_icon_hitbox = pygame.Rect((698, 470), (75, 95))
                        if account == "michael":
                            screen.blit(mail_icon, (438, 315))
                            mail_icon_hitbox = pygame.Rect((438, 315), (75, 95))
                            screen.blit(notes_icon, (588, 325))
                            notes_icon_hitbox = pygame.Rect((588, 325), (75, 95))
                            screen.blit(music_icon, (504, 420))
                            music_icon_hitbox = pygame.Rect((504, 420), (75, 95))
                            screen.blit(photos_icon, (640, 460))
                            photos_icon_hitbox = pygame.Rect((640, 460), (75, 95))
                        if account == "john":
                            screen.blit(notes_icon, (317, 240))
                            notes_icon_hitbox = pygame.Rect((317, 240), (75, 95))
                            screen.blit(music_icon, (320, 330))
                            music_icon_hitbox = pygame.Rect((320, 330), (75, 95))
                            screen.blit(photos_icon, (310, 420))
                            photos_icon_hitbox = pygame.Rect((310, 420), (75, 95))
                            screen.blit(mail_icon, (867, 510))
                            mail_icon_hitbox = pygame.Rect((867, 510), (75, 95))
                        if account == "marion":
                            screen.blit(notes_icon, (592, 375))
                            notes_icon_hitbox = pygame.Rect((592, 375), (75, 95))
                            pygame.mixer.music.load(
                                "Assets/Audio Assets/ominous-loop.mp3"
                            )
                            pygame.mixer.music.play(-1)

                        screen.blit(logout_icon, (285, 665))
                        screen.blit(outside, (0, 0))
                    password_input = ""

            password = body_text.render(password_input, True, (0, 0, 0))

            if (
                event.type == pygame.TEXTINPUT
                and password.get_width() < 240
                and password_active == True
            ):
                password_input += event.text

            if password_active:
                password_color = password_color_active
            else:
                password_color = password_color_passive

            if account == "no one":
                screen.blit(password_prompt, password_prompt_rect)
                pygame.draw.rect(screen, password_color, password_input_rect)
                screen.blit(hint_prompt, hint_prompt_rect)

            screen.blit(
                password, (password_input_rect.x + 5, password_input_rect.y + 5)
            )

            if hint_prompt_rect.collidepoint(point) and mouse_left:
                hint = True
            if hint:
                if account_selected == "nicole":
                    hint_prompt = body_text.render(
                        "Need a hint?\nIt's the first thing you think of!",
                        True,
                        (255, 255, 255),
                    )
                if account_selected == "michael":
                    hint_prompt = body_text.render(
                        "Need a hint?\ngreatest accomplishment + grad year",
                        True,
                        (255, 255, 255),
                    )
                if account_selected == "john":
                    hint_prompt = body_text.render(
                        "Need a hint?\nMcD0nald's astr0naut", True, (255, 255, 255)
                    )
                if account_selected == "marion":
                    hint_prompt = body_text.render(
                        "Need a hint?\n3rd November 1967", True, (255, 255, 255)
                    )
                if mouse_left and not hint_prompt_rect.collidepoint(point):
                    hint_prompt = body_text.render(
                        "Need a hint?", True, (255, 255, 255)
                    )
                    hint = False

        if account != "no one":

            pygame.draw.rect(screen, (230, 235, 240), clock_display_rect)
            screen.blit(clock_display, clock_display_rect)

            if logout_hitbox.collidepoint(point) and mouse_left:
                account = "no one"
                account_selected = "no one"
                pygame.time.delay(900)
                pygame.mixer.music.stop()
                screen.blit(login_screen, (276, 165))
                screen.blit(outside, (0, 0))

            if mail_icon_hitbox.collidepoint(point) and mouse_left:
                mail_open = True
                screen.blit(mail_UI)

            if music_icon_hitbox.collidepoint(point) and mouse_left:
                music_open = True
                if pygame.mixer.music.get_busy() == False:
                    pygame.mixer.music.load("Assets/Audio Assets/moremusic.mp3")
                    screen.blit(music_paused_UI, (400, 200))
                else:
                    screen.blit(music_playing_UI, (400, 200))

            if notes_icon_hitbox.collidepoint(point) and mouse_left:
                notes_open = True
                screen.blit(notes_UI)

    current_time = datetime.datetime.now()
    second = (60 + int(current_time.strftime("%S")) - init_second) % 60
    if second < 10:
        second = "0" + str(second)
    minute = 3 + ((60 + int(current_time.strftime("%M")) - init_minute) % 60)
    if minute < 10:
        minute = "0" + str(minute)
    hour = 11 + ((12 + int(current_time.strftime("%I")) - init_hour) % 12)
    if hour < 10:
        hour = "0" + str(hour)
    if hour > 11:
        meridian = "AM"
        clock_display = body_text.render(
            "January 1, 2000, "
            + str(hour)
            + ":"
            + str(minute)
            + ":"
            + str(second)
            + " "
            + meridian,
            True,
            (0, 0, 0),
        )
    else:
        meridian = "PM"
        clock_display = body_text.render(
            "December 31, 1999, "
            + str(hour)
            + ":"
            + str(minute)
            + ":"
            + str(second)
            + " "
            + meridian,
            True,
            (0, 0, 0),
        )
    if account != "no one":
        pygame.draw.rect(screen, (230, 235, 240), clock_display_rect)
        screen.blit(clock_display, clock_display_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
