import pygame
import datetime

pygame.init()
pygame.mixer.init()
braammmm = pygame.mixer.Sound("Assets/Audio Assets/braammmm.wav")
fireworks = pygame.mixer.Sound("Assets/Audio Assets/Fireworks.mp3")
pygame.mixer.music.load("Assets/Audio Assets/moremusic.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.pause()
flags = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode((1244, 900), flags)
pygame.display.set_caption("Eleventh Hour")
clock = pygame.time.Clock()
running = True

arm = pygame.image.load("Assets/Image Assets/Arm.png").convert_alpha()
backdrop = pygame.image.load("Assets/Image Assets/Computer Backdrop.png").convert_alpha()
login_screen = pygame.image.load("Assets/Image Assets/Login Screen.png").convert_alpha()
nicole_pfp = pygame.image.load("Assets/Image Assets/Nicole pfp.png").convert_alpha()
michael_pfp = pygame.image.load("Assets/Image Assets/Michael pfp.png").convert_alpha()
john_pfp = pygame.image.load("Assets/Image Assets/John pfp.png").convert_alpha()
marion_pfp = pygame.image.load("Assets/Image Assets/Marion pfp.png").convert_alpha()
outside = pygame.image.load("Assets/Image Assets/Lost And Forgotten.png").convert_alpha()
mail_UI = pygame.image.load("Assets/Image Assets/Mail UI.png").convert_alpha()
mail_back = pygame.image.load("Assets/Image Assets/Mail Back Button.png").convert_alpha()
music_paused_UI = pygame.image.load("Assets/Image Assets/Music UI.png").convert_alpha()
music_playing_UI = pygame.image.load("Assets/Image Assets/Music UI (playing).png").convert_alpha()
notes_UI = pygame.image.load("Assets/Image Assets/Notes UI.png").convert_alpha()
notes_back = pygame.image.load("Assets/Image Assets/Notes Back Button.png").convert_alpha()
photos_UI = pygame.image.load("Assets/Image Assets/Photos UI.png").convert_alpha()
nicole_photo_1 = pygame.image.load("Assets/Image Assets/Nicole Photo 1.png").convert_alpha()
nicole_photo_2 = pygame.image.load("Assets/Image Assets/Nicole Photo 2.png").convert_alpha()
nicole_photo_3 = pygame.image.load("Assets/Image Assets/Nicole Photo 3.png").convert_alpha()
michael_photo_1 = pygame.image.load("Assets/Image Assets/Michael Photo 1.png").convert_alpha()
michael_photo_2 = pygame.image.load("Assets/Image Assets/Michael Photo 2.png").convert_alpha()
michael_photo_3 = pygame.image.load("Assets/Image Assets/Michael Photo 3.png").convert_alpha()
john_photo_1 = pygame.image.load("Assets/Image Assets/john Photo 1.png").convert_alpha()
john_photo_2 = pygame.image.load("Assets/Image Assets/john Photo 2.png").convert_alpha()
john_photo_3 = pygame.image.load("Assets/Image Assets/john Photo 3.png").convert_alpha()
logout_icon = pygame.image.load("Assets/Image Assets/Exit Icon.png").convert_alpha()
mail_icon = pygame.image.load("Assets/Image Assets/Mail Icon.png").convert_alpha()
music_icon = pygame.image.load("Assets/Image Assets/Music Icon.png").convert_alpha()
notes_icon = pygame.image.load("Assets/Image Assets/Notes Icon.png").convert_alpha()
photos_icon = pygame.image.load("Assets/Image Assets/Photos Icon.png").convert_alpha()
mail_icon = pygame.transform.scale(mail_icon, (75, 95))
mail_back = pygame.transform.scale(mail_back, (40, 40))
music_icon = pygame.transform.scale(music_icon, (75, 95))
notes_icon = pygame.transform.scale(notes_icon, (75, 95))
notes_back = pygame.transform.scale(notes_back, (40, 40))
photos_icon = pygame.transform.scale(photos_icon, (75, 95))
outside = pygame.transform.scale(outside, (1244, 900))

power_hitbox = pygame.Rect((908, 780), (33, 33))
nicole_hitbox = pygame.Rect((305, 260), (200, 70))
michael_hitbox = pygame.Rect((305, 360), (200, 70))
john_hitbox = pygame.Rect((305, 460), (200, 70))
marion_hitbox = pygame.Rect((305, 560), (200, 70))
logout_hitbox = pygame.Rect((285, 665), (60, 60))
UI_Exit_hitbox = pygame.Rect((795,200,60,60))
mail_icon_hitbox = pygame.Rect((0, 0), (0, 0))
music_icon_hitbox = pygame.Rect((0, 0), (0, 0))
notes_icon_hitbox = pygame.Rect((0, 0), (0, 0))
photos_icon_hitbox = pygame.Rect((0, 0), (0, 0))
music_play_hitbox = pygame.Rect((580, 470), (100, 100))
back_hitbox = pygame.Rect((420, 520), (40, 40))
mail_1_hitbox = pygame.Rect((420, 270), (420, 40))
mail_2_hitbox = pygame.Rect((420, 320), (420, 40))
mail_3_hitbox = pygame.Rect((420, 370), (420, 40))
mail_4_hitbox = pygame.Rect((420, 420), (420, 40))
mail_5_hitbox = pygame.Rect((420, 470), (420, 40))
mail_6_hitbox = pygame.Rect((420, 520), (420, 40))
note_1_hitbox = pygame.Rect((410, 260), (140, 150))
note_2_hitbox = pygame.Rect((560, 260), (140, 150))
note_3_hitbox = pygame.Rect((710, 260), (140, 150))
note_4_hitbox = pygame.Rect((410, 420), (140, 150))
note_5_hitbox = pygame.Rect((560, 420), (140, 150))
note_6_hitbox = pygame.Rect((710, 420), (140, 150))
photos_left_hitbox = pygame.Rect((408, 380), (60, 60))
photos_right_hitbox = pygame.Rect((793, 380), (60, 60))
# photos_left_hitbox = pygame.Rect((420, 300), (60, 60))

cursor_x = 0
cursor_y = 0
computer_on = False
account = "no one"
account_selected = "no one"
hint = False
nicole_password = ""
clock_text = ""
music_open = False
mail_open = False
reading_mail = False
notes_open = False
reading_notes = False
photos_open = False
photo = 1
dummy = 0
game_over = False
were_in_the_endframe_now = 0

pygame.mouse.set_visible(False)

password_input = ""
password_active = False
password_color_active = pygame.Color((255, 255, 255))
password_color_passive = pygame.Color((200, 200, 200))
password_color = password_color_passive

screen.fill("#302732")
screen.blit(outside, (0, 0))

pygame.font.init()
# tahoma = pygame.font.Font = "Assets/Image Assets/tahoma.ttf"
header = pygame.font.SysFont('tahoma', 18)
body_text = pygame.font.SysFont('tahoma', 12)


login_prompt = header.render("To begin, click on your profile", True, (255, 255, 255))
login_prompt_rect = login_prompt.get_rect()
login_prompt_rect.center = (740, 550)

password_prompt = body_text.render("Password:", True, (255, 255, 255))
password_prompt_rect = password_prompt.get_rect()
password_prompt_rect.center = (650, 525)


nicole_note_1_date = body_text.render("Nov 8, 98\n    12:40 PM", True, (0, 0, 0))
nicole_note_1_date_rect = nicole_note_1_date.get_rect()
nicole_note_1_date_rect.center = (480, 335)

nicole_note_1 = body_text.render("I guess I could only put off getting this set up for so long. Somehow using\nMichael's computer feels like I'm giving up on him. I know that's stupid,\nbut... it still feels like it. But hey, free computer. It's old as hell and\nbroke as ass, but seems like it'll be useful. I had to make a guest account\nbecause there's already a bunch of other accounts on here, not just Michael's.\nI wonder who they are.\n\n", True, (0, 0, 0))
nicole_note_1_rect = nicole_note_1.get_rect()
nicole_note_1_rect.center = (630, 415)

nicole_note_2_date = body_text.render("Nov 19, 98\n    12:57 AM", True, (0, 0, 0))
nicole_note_2_date_rect = nicole_note_2_date.get_rect()
nicole_note_2_date_rect.center = (630, 335)

nicole_note_2 = body_text.render("I think this computer is haunted. Not actually, but. It might have a virus\nor something.\n\nI guess I should be using this as a diary or something? Not much to say.\nStill unemployed, still broke, still no idea what I'm doing. Why the fuck\ndid I go to grad school for visual art? Where am I supposed to go\nfrom here?", True, (0, 0, 0))
nicole_note_2_rect = nicole_note_2.get_rect()
nicole_note_2_rect.center = (630, 415)

nicole_note_3_date = body_text.render("Dec 25, 98\n    11:39 PM", True, (0, 0, 0))
nicole_note_3_date_rect = nicole_note_3_date.get_rect()
nicole_note_3_date_rect.center = (780, 335)

nicole_note_3 = body_text.render("It's weird how I spent most of my childhood not celebrating Christmas, and\nnow it's the loneliest thing in the world to not have someone to\nexchange gifts with.\n\nI bought myself a bar of chocolate and some new socks. Fuck, I'm already\ngetting old.\n\nOh, I figured out the computer thing. There's a program called Marion\nthat just kind of... does stuff, sometimes. I can't tell if it has a purpose\nor if it's just clicking on random things. Weird.", True, (0, 0, 0))
nicole_note_3_rect = nicole_note_3.get_rect()
nicole_note_3_rect.center = (630, 415)

nicole_note_4_date = body_text.render("Jun 6, 99\n    3:44 PM", True, (0, 0, 0))
nicole_note_4_date_rect = nicole_note_4_date.get_rect()
nicole_note_4_date_rect.center = (480, 495)

nicole_note_4 = body_text.render("Hi! Um... Marion, right? I mean, that's the name of the app running in the\nbackground. I assume that's you. Computer. I don't know if you can\nread this, but. Anyway - Michael was supposed to graduate today, and\nhe's... um... gone... but since he got us kicked out of my own grad party\nI thought I should at least do something for his. So... I'm going to get\nreally drunk. In his honor. Since that's what he did for me. Marion,\nyou're my witness that I got fucked up for him. Cheers, babe.", True, (0, 0, 0))
nicole_note_4_rect = nicole_note_4.get_rect()
nicole_note_4_rect.center = (630, 415)

nicole_note_5_date = body_text.render("Sep 30, 99\n    2:13 AM", True, (0, 0, 0))
nicole_note_5_date_rect = nicole_note_5_date.get_rect()
nicole_note_5_date_rect.center = (630, 495)

nicole_note_5 = body_text.render("People have been talking a lot about how Y2K could be the end of the world.\nNot just the digital world, but everything. I don't really get it, to be\nhonest, but... hey, there's something comforting in living to see the end\nof the world. I guess we'll see in a few months.", True, (0, 0, 0))
nicole_note_5_rect = nicole_note_5.get_rect()
nicole_note_5_rect.center = (630, 415)

nicole_note_6_date = body_text.render("Dec 31, 99\n    6:02 PM", True, (0, 0, 0))
nicole_note_6_date_rect = nicole_note_6_date.get_rect()
nicole_note_6_date_rect.center = (780, 495)

nicole_note_6 = body_text.render("So this is it. Six hours left.\n\nNot sure how this is going to happen. If it'll take a few months or happen\nall at once. Probably not all at once, but I guess you never know.\n\nIf we do get a while longer, it's not going to be with many computers. I\ntried setting the system clock on this computer back to 1900, but for\nsome reason only the system administrator can do that. It's too bad, this\ncomputer is terrible, but Marion's growing on me. I hope they don't see\nthis as death, since they're a program.\n\nBut I guess that's what it is.", True, (0, 0, 0))
nicole_note_6_rect = nicole_note_6.get_rect()
nicole_note_6_rect.center = (630, 415)

michael_note_1_date = body_text.render("Sep 2, 95\n    5:11 PM", True, (0, 0, 0))
michael_note_1_date_rect = michael_note_1_date.get_rect()
michael_note_1_date_rect.center = (480, 335)

michael_note_1 = body_text.render("okay huh. why does this app exist. like literally whats the point just\nuse paper. can you even save more than six notes?", True, (0, 0, 0))
michael_note_1_rect = michael_note_1.get_rect()
michael_note_1_rect.center = (630, 415)

michael_note_2_date = body_text.render("Sep 29, 95", True, (0, 0, 0))
michael_note_2_date_rect = michael_note_2_date.get_rect()
michael_note_2_date_rect.center = (630, 335)

michael_note_2 = body_text.render("its nice to be given this now that im starting med school and gonna be a\ndoctor and everything, dont get me wrong. having a computer is way more\nhelpful than i expected.\n\nand in some ways its like johns passing the mantle onto me, i guess\n\nbut it feels more like giving up on him. i know he agreed i could have\nit, but i dont know if he knows that. i dont know what he knows anymore", True, (0, 0, 0))
michael_note_2_rect = michael_note_2.get_rect()
michael_note_2_rect.center = (630, 415)

michael_note_3_date = body_text.render("Jul 1, 96", True, (0, 0, 0))
michael_note_3_date_rect = michael_note_3_date.get_rect()
michael_note_3_date_rect.center = (780, 335)

michael_note_3 = body_text.render("john had a relatively lucid day, today. A little bit of cool uncle came\nback. its been a while since hes had one of those. we got to take him\non a walk, go out for lunch.\n\nit was really nice.", True, (0, 0, 0))
michael_note_3_rect = michael_note_3.get_rect()
michael_note_3_rect.center = (630, 415)

michael_note_4_date = body_text.render("Jan 28, 97", True, (0, 0, 0))
michael_note_4_date_rect = michael_note_4_date.get_rect()
michael_note_4_date_rect.center = (480, 495)

michael_note_4 = body_text.render("itoobk tooo many ebidles and lmao why r they callde horse girsl intead of\nhorsis\n\nn if ur a guy. brorses", True, (0, 0, 0))
michael_note_4_rect = michael_note_4.get_rect()
michael_note_4_rect.center = (630, 415)

michael_note_5_date = body_text.render("Feb 13, 98", True, (0, 0, 0))
michael_note_5_date_rect = michael_note_5_date.get_rect()
michael_note_5_date_rect.center = (630, 495)

michael_note_5 = body_text.render("fuck", True, (0, 0, 0))
michael_note_5_rect = michael_note_5.get_rect()
michael_note_5_rect.center = (630, 415)

michael_note_6_date = body_text.render("Feb 14, 98", True, (0, 0, 0))
michael_note_6_date_rect = michael_note_6_date.get_rect()
michael_note_6_date_rect.center = (780, 495)

michael_note_6 = body_text.render("ok so pancreatic cancer is one of the most dangerous forms of cancer. due to\nbeing typically asymptomatic until progressing to late stage, when its\nmost difficult to treat. and at that point, the best thing you can do\nis lie about their chances. laughter isn't the best medicine, hope is. and\nthree and a half years of medical school have told me how hopeless my case is.\n\nim gonna die. fuck, im gonna die. ...ok. why not? the world might be\nending in two years anyway, that's what nicky thinks. maybe I just got a\nheadstart on it. always the fucking\ngo-getter, thats me. woooo.\n\ni think im gonna do something. not sure what yet. drop out of med school,\nprobably. dont want to spend my last four to eight months doing sub-internship\napplications. then... hey, im young, ive got a savings account, i dont have\na will. maybe ill get an rv, drop off the grid, get high somewhere where\nits legal. or where it isnt, it doesn't matter. just drive off into the sunset.\n\n                     i guess ive always wanted to see the ocean.", True, (0, 0, 0))
michael_note_6_rect = michael_note_6.get_rect()
michael_note_6_rect.center = (630, 415)

john_note_1_date = body_text.render("Mar 19, 91", True, (0, 0, 0))
john_note_1_date_rect = john_note_1_date.get_rect()
john_note_1_date_rect.center = (480, 335)

john_note_1 = body_text.render("I guess I must have deleted my account on accident! Odd. It's a shame that I\nlost all of my pictures and notes. I wonder if I'll be able to remember\nany of them. Maybe I could ask Marion next time I see him.", True, (0, 0, 0))
john_note_1_rect = john_note_1.get_rect()
john_note_1_rect.center = (630, 415)

john_note_2_date = body_text.render("Jan 12, 92", True, (0, 0, 0))
john_note_2_date_rect = john_note_2_date.get_rect()
john_note_2_date_rect.center = (630, 335)

john_note_2 = body_text.render("It's certainly strange, losing grip on my memories, like this. Slowly. I\ndon't remember what I don't remember! I've been wanting to call Marion,\nbut I can't remember her number, or if we've spoken recently. I try to\nmake light of it, since the alternative is", True, (0, 0, 0))
john_note_2_rect = john_note_2.get_rect()
john_note_2_rect.center = (630, 415)

john_note_3_date = body_text.render("Dec 8, 92", True, (0, 0, 0))
john_note_3_date_rect = john_note_3_date.get_rect()
john_note_3_date_rect.center = (780, 335)

john_note_3 = body_text.render("I wrote a computer program today! Very basic stuff, but at least it's\nsomething I was able to remember. Each time you click, the mouse changes\ncolor! Fun. Marion would have loved it.", True, (0, 0, 0))
john_note_3_rect = john_note_3.get_rect()
john_note_3_rect.center = (630, 415)

john_note_4_date = body_text.render("Oct 30, 93", True, (0, 0, 0))
john_note_4_date_rect = john_note_4_date.get_rect()
john_note_4_date_rect.center = (480, 495)

john_note_4 = body_text.render("This computer sure has a mind of its own, sometimes! Perhaps it's haunted - it\nmatches the time of year! Ha. I got this computer from Marion, didn't I?\nI can't remember, but it makes sense, given that her account is the\nsysadmin. I wonder where Marion got it from!", True, (0, 0, 0))
john_note_4_rect = john_note_4.get_rect()
john_note_4_rect.center = (630, 415)

john_note_5_date = body_text.render("May 1, 94", True, (0, 0, 0))
john_note_5_date_rect = john_note_5_date.get_rect()
john_note_5_date_rect.center = (630, 495)

john_note_5 = body_text.render("I used to be so good with computers! I caught myself unable to convert even\nthe simplest of sentences into binary. I decided to practice: we're\nstarting with the basics, numbers! I admit I saved a cheat sheet somewhere.\n\nWas Marion good with computers? Maybe I should ask him for help.", True, (0, 0, 0))
john_note_5_rect = john_note_5.get_rect()
john_note_5_rect.center = (630, 415)

john_note_6_date = body_text.render("Jul 20, 95", True, (0, 0, 0))
john_note_6_date_rect = john_note_6_date.get_rect()
john_note_6_date_rect.center = (780, 495)

john_note_6 = body_text.render("Who is Marion?", True, (0, 0, 0))
john_note_6_rect = john_note_6.get_rect()
john_note_6_rect.center = (630, 415)

marion_note_1_date = body_text.render("Sep 19, 90", True, (0, 0, 0))
marion_note_1_date_rect = marion_note_1_date.get_rect()
marion_note_1_date_rect.center = (480, 335)

marion_note_1 = body_text.render("09 19 90\n\nLots of 9s in today's date! Date puzzle: log_9(1) = 9-9. Tricky!\n\nIt's been a good day. Made lots of progress on the program. I found a\nrecipe for a sort of orange cake I'm curious about. We'll see if it's any\ngood! I plan on making it over the weekend. I like to imagine that Marion\nwould have been a good baker.", True, (0, 0, 0))
marion_note_1_rect = marion_note_1.get_rect()
marion_note_1_rect.center = (630, 415)

marion_note_2_date = body_text.render("Sep 20, 90", True, (0, 0, 0))
marion_note_2_date_rect = marion_note_2_date.get_rect()
marion_note_2_date_rect.center = (630, 335)

marion_note_2 = body_text.render("09 20 90\n\nNot enough nonzero entries for the date puzzle! A shame.\nIt's been cooling down quite a bit! I'm going to need my heavy jacket\nsoon. Also, workaround I came up with yesterday has a major bug I noticed\ntoday. Frustrating! Spent many hours with no progress on that issue.\nAlso, I am much worse at Mario 3 than its predecessor, at least for now.\nWill change with time!\nOne of the things I mourn the most regarding Marion is that growing up,\nI never had anyone to play games with.", True, (0, 0, 0))
marion_note_2_rect = marion_note_2.get_rect()
marion_note_2_rect.center = (630, 415)

marion_note_3_date = body_text.render("Sep 22, 90", True, (0, 0, 0))
marion_note_3_date_rect = marion_note_3_date.get_rect()
marion_note_3_date_rect.center = (780, 335)

marion_note_3 = body_text.render("09 22 90\nI completely forgot to write an entry for yesterday! Sorry, Earth, Wind &\nFire. Things have been slipping my mind more and more frequently,\nlately. I suppose that's aging for you!\nGave up on bug from before, will come back later, making good progress in\nthe meantime. I have so many oranges! Where did they all come from?", True, (0, 0, 0))
marion_note_3_rect = marion_note_3.get_rect()
marion_note_3_rect.center = (630, 415)

marion_note_4_date = body_text.render("Oct 4, 90", True, (0, 0, 0))
marion_note_4_date_rect = marion_note_4_date.get_rect()
marion_note_4_date_rect.center = (480, 495)

marion_note_4 = body_text.render("It works! Marion works! Look at you go, this is incredible. Progress has\nbeen very slow recently, restricted to my good days. I am very\nfortunate that most of the work was completed before the start of\nmy decline. And sure, there is no practical application to having an\narguably self-aware program with full user access, but you have to admit\nthat this is rather exciting.", True, (0, 0, 0))
marion_note_4_rect = marion_note_4.get_rect()
marion_note_4_rect.center = (630, 415)

marion_note_5_date = body_text.render("Dec 28, 90", True, (0, 0, 0))
marion_note_5_date_rect = marion_note_5_date.get_rect()
marion_note_5_date_rect.center = (630, 495)

marion_note_5 = body_text.render("Michael has a new friend. I'm happy for my nephew, and for her as well. I\nhope I can get to know her better while I still have time.\nMy decline is concerning. Today is a better day than I've had in\nmonths. What delusions will I have come the New Year? What delusions\ndo I hold now?\nNicole is her name. I will try to remember.", True, (0, 0, 0))
marion_note_5_rect = marion_note_5.get_rect()
marion_note_5_rect.center = (630, 415)

marion_note_6_date = body_text.render("May 10, 91", True, (0, 0, 0))
marion_note_6_date_rect = marion_note_6_date.get_rect()
marion_note_6_date_rect.center = (780, 495)

marion_note_6 = body_text.render("It has been a long time since I've been lucid. I should be frightened,\nbut I am only embarrassed and exhausted. Perhaps I was never sane.\nWho in their right mind would live their whole life obsessed with a\ntwin they never had? I made an account for them instead of myself, I\nspent years writing a program to pretend that they were alive... it's\nlittle wonder that I muddled the facts in my decline.\nMy mother has no children left: Marion stillborn, myself nothing but the\nshell of her son.", True, (0, 0, 0))
marion_note_6_rect = marion_note_6.get_rect()
marion_note_6_rect.center = (630, 415)


nicole_mail_1_label = body_text.render("<michael&jello@mail.com> PARTY PARTY PARTY Jun 22 97", True, (0, 0, 0))
nicole_mail_1_label_rect = nicole_mail_1_label.get_rect()
nicole_mail_1_label_rect.topleft = (430, 282)

nicole_mail_1 = body_text.render("From <michael&jello@mail.com>: PARTY PARTY PARTY\n\nNICKY okay you remember me telling you about sasha? shes literally the best\ni think shes on drugs like 90% of the time. anyway shes throwing a party\ntonight and you should totally come if you can, its going to be terrible\nand im going to get sooo drunk lol (im pregaming a lil, can u tell?)\n\nsigned,\nTHE KEGSMASHER", True, (0, 0, 0))
nicole_mail_1_rect = nicole_mail_1.get_rect()
nicole_mail_1_rect.topleft = (420, 270)

nicole_mail_2_label = body_text.render("<izumito@mail.com> We Got a Computer Feb 28 98", True, (0, 0, 0))
nicole_mail_2_label_rect = nicole_mail_2_label.get_rect()
nicole_mail_2_label_rect.topleft = (430, 332)

nicole_mail_2 = body_text.render("From <izumito@mail.com>: We Got a Computer\n\nDear Nicole,\n\nHello! I hope you're doing well.\n\nGuess what? My dad got a computer for his work! He's letting us use it\nwhen he's not busy. So I can send you E-mails now! I hope I remembered your\nE-mail address correctly.\n\nSigned,\nIzumi Ito", True, (0, 0, 0))
nicole_mail_2_rect = nicole_mail_2.get_rect()
nicole_mail_2_rect.topleft = (420, 270)

nicole_mail_3_label = body_text.render("<michael&jello@mail.com> RE:Graduation Party!! Jun 2 98", True, (0, 0, 0))
nicole_mail_3_label_rect = nicole_mail_3_label.get_rect()
nicole_mail_3_label_rect.topleft = (430, 382)

nicole_mail_3 = body_text.render("From <michael&jello@mail.com>: RE:Graduation Party!!\n\nholy shit i cant believe youre graduating next week! yes obviously im going to\nbe there i cant believe youd even consider otherwise. question: will\nthere be booze? because i know a gal, and we can make it that kinda party\nif you want to lol. if you want this to be a Nice Proper little thing id\nbe happy to stay sober and wear something nice and whatever but if you\nwant it to be a actual celebration, im fucking proud of the title\nkegsmasher and im going to use it\n\nmichael", True, (0, 0, 0))
nicole_mail_3_rect = nicole_mail_3.get_rect()
nicole_mail_3_rect.topleft = (420, 270)

nicole_mail_4_label = body_text.render("<michael&jello@mail.com> RE:RE:bad news Sep 19 98", True, (0, 0, 0))
nicole_mail_4_label_rect = nicole_mail_4_label.get_rect()
nicole_mail_4_label_rect.topleft = (430, 432)

nicole_mail_4 = body_text.render("From <michael&jello@mail.com>: RE:RE:bad news\n\nyeah. im sorry to spring this on you like this, but... yeah, it doesnt look good.\n\nim scared, nicole. im really fucking scared\n\nthis isnt how it was supposed to go", True, (0, 0, 0))
nicole_mail_4_rect = nicole_mail_4.get_rect()
nicole_mail_4_rect.topleft = (420, 270)

nicole_mail_5_label = body_text.render("<michael&jello@mail.com> leaving Oct 12 98", True, (0, 0, 0))
nicole_mail_5_label_rect = nicole_mail_5_label.get_rect()
nicole_mail_5_label_rect.topleft = (430, 482)

nicole_mail_5 = body_text.render("From <michael&jello@mail.com>: leaving\n\nhey nicky\n\ni think im going to be ready to leave by saturday. still want me to come by\ntomorrow and give you my old computer and stuff?\n\nwe could also go into town and get sodas or something. or go to the lake\nagain. one last goodbye, i guess?\n\nmichael", True, (0, 0, 0))
nicole_mail_5_rect = nicole_mail_5.get_rect()
nicole_mail_5_rect.topleft = (420, 270)

nicole_mail_6_label = body_text.render("<izumito@mail.com> Checking In Oct 20 98", True, (0, 0, 0))
nicole_mail_6_label_rect = nicole_mail_6_label.get_rect()
nicole_mail_6_label_rect.topleft = (430, 532)

nicole_mail_6 = body_text.render("From <izumito@mail.com>: Checking In\n\nHi, Nicole!\n\nI thought I'd try to send you an E-mail since you weren't answering the phone.\nIs everything okay? Are we still trick-or-treating together?\n\nSigned,\nIzumi", True, (0, 0, 0))
nicole_mail_6_rect = nicole_mail_6.get_rect()
nicole_mail_6_rect.topleft = (420, 270)

michael_mail_1_label = body_text.render("<johnatron@mail.com> Hi, Michael! May 10 91", True, (0, 0, 0))
michael_mail_1_label_rect = michael_mail_1_label.get_rect()
michael_mail_1_label_rect.topleft = (430, 282)

michael_mail_1 = body_text.render("From <johnatron@mail.com>: Hi, Michael!\n\nJust wanted to check in and say hi. It's been a while! Any chance you'd\nbe down to grab sodas in town or rescue Peach or anything?\n\nUncle John", True, (0, 0, 0))
michael_mail_1_rect = michael_mail_1.get_rect()
michael_mail_1_rect.topleft = (420, 270)

michael_mail_2_label = body_text.render("<nicolecat@mail.com> :D :P Jan 21 93", True, (0, 0, 0))
michael_mail_2_label_rect = michael_mail_2_label.get_rect()
michael_mail_2_label_rect.topleft = (430, 332)

michael_mail_2 = body_text.render("From <nicolecat@mail.com>: :D :P\n\nHeyyy I got let into the computer lab lol.\n\nAlso we need to call once you're out of lab because there's this girl in\nmy photography class and I need you to ask her out so I can learn if she's\ninto girls or not. I can't ask because she's scary.", True, (0, 0, 0))
michael_mail_2_rect = michael_mail_2.get_rect()
michael_mail_2_rect.topleft = (420, 270)

michael_mail_3_label = body_text.render("<johnatron@mail.com> RE:secret of DOOM! Mar 10 95", True, (0, 0, 0))
michael_mail_3_label_rect = michael_mail_3_label.get_rect()
michael_mail_3_label_rect.topleft = (430, 382)

michael_mail_3 = body_text.render("From <johnatron@mail.com>: RE:secret of DOOM!\n\nHi, Miguel! I was just thinking about you. I've never played Doom, let alone the\nsequel, but that's a funny secret! Reminds me of my favorite \"Easter Egg\" - in\nMoonlander, you can fly to a secret McDonald's on the moon and your\ncharacter will stop to get food! Apologies if I've already told you about that\none. I think it's hilarious :)\n\nI hope your classes are all going well! You've always been a smart kid.\n\nUncle John\n\nP.S. Speaking of videogames - happy MAR10 day!", True, (0, 0, 0))
michael_mail_3_rect = michael_mail_3.get_rect()
michael_mail_3_rect.topleft = (420, 270)

michael_mail_4_label = body_text.render("<rgutman@caduceusbiomedical.com> Application Denied Apr 2 97", True, (0, 0, 0))
michael_mail_4_label_rect = michael_mail_4_label.get_rect()
michael_mail_4_label_rect.topleft = (430, 432)

michael_mail_4 = body_text.render("From <rgutman@caduceusbiomedical.com>: Application Denied\n\nHello, Michael.\n\nWe regret to inform you that we will not be accepting your application\nto intern at Caedacus Biomedical Wellness at this time. While you are\nan accomplished student and seem very qualified for one of our internship\npositions, your unprofessional behavior and disregard for basic ettiquite\nmake you an undesireable candidate. In the future, we advice against\nwriting your application in comic sans bold, abstaining from capitalization\nor punctuation, and signing off your emails with \"mic drop.\" We wish\nyou luck in future applications.\n\nCaduceus Biomedical Wellness", True, (0, 0, 0))
michael_mail_4_rect = michael_mail_4.get_rect()
michael_mail_4_rect.topleft = (420, 270)

michael_mail_5_label = body_text.render("<sashayaway@mail.com> RE:bye Feb 13 98", True, (0, 0, 0))
michael_mail_5_label_rect = michael_mail_5_label.get_rect()
michael_mail_5_label_rect.topleft = (430, 482)

michael_mail_5 = body_text.render("From <sashayaway@mail.com>: RE:bye\n\nmichael? what the fuck do you mean 'bye' get back here bitch. are you okay?\nare you in trouble? look, if the whole valentine's thing was too much\nthen i'll dial it back, we can do something small or do nothing at all.\ni don't want to put you through anything you're not ready for.\n\ni... i care about you, michael. a lot. i'm sorry for freaking out, i\njust... you're scaring me a bit. you'd better message me back, asshole.\n\nsasha", True, (0, 0, 0))
michael_mail_5_rect = michael_mail_5.get_rect()
michael_mail_5_rect.topleft = (420, 270)

michael_mail_6_label = body_text.render("<nicolecat@mail.com> I miss you Mar 2 99", True, (0, 0, 0))
michael_mail_6_label_rect = michael_mail_6_label.get_rect()
michael_mail_6_label_rect.topleft = (430, 532)

michael_mail_6 = body_text.render("From <nicolecat@mail.com>: I miss you\n\nI wonder if you miss me.", True, (0, 0, 0))
michael_mail_6_rect = michael_mail_6.get_rect()
michael_mail_6_rect.topleft = (420, 270)

john_mail_1_label = body_text.render("<rgutman@caduceusbiomedical.com> Results In Oct 1 90", True, (0, 0, 0))
john_mail_1_label_rect = john_mail_1_label.get_rect()
john_mail_1_label_rect.topleft = (430, 282)

john_mail_1 = body_text.render("From <rgutman@caduceusbiomedical.com>: Results In\n\nDear John Dedisc\n\nWe regret to inform you that your recent checkup has shown signs of early-\nonset dementia and gray matter decay. We recommend scheduling a followup\nappointment so we can learn more about the cause, progression, and\npotential treatment for your affliction.\n\nCaduceus Biomedical Wellness", True, (0, 0, 0))
john_mail_1_rect = john_mail_1.get_rect()
john_mail_1_rect.topleft = (420, 270)

john_mail_2_label = body_text.render("<desmondc@mail.com> \"Technology Apocalypse\" Concern Jan 7 91", True, (0, 0, 0))
john_mail_2_label_rect = john_mail_2_label.get_rect()
john_mail_2_label_rect.topleft = (430, 332)

john_mail_2 = body_text.render("From <desmondc@mail.com>: \"Technology Apocalypse\" Concern\n\nHello, John\n\nAt a conference, I recently overheard two computer scientists discussing a\npotential \"apocalypse\" in the coming years caused by a collapse in all\ndigitized systems that rely on accurate timekeeping, at turn of the\nmillenia. What are your thoughts on the matter, could the world really come\nto ruin because of this?\n\nI, for one, have no doubts that that it could and shall.\n\nDesmond Creed", True, (0, 0, 0))
john_mail_2_rect = john_mail_2.get_rect()
john_mail_2_rect.topleft = (420, 270)

john_mail_3_label = body_text.render("<michael&jello@mail.com> movie night? Nov 3, 92", True, (0, 0, 0))
john_mail_3_label_rect = john_mail_3_label.get_rect()
john_mail_3_label_rect.topleft = (430, 382)

john_mail_3 = body_text.render("From <michael&jello@mail.com>: movie night?\n\nhey uncle john!\n\ni meant to send this yesterday but i forgot. do you have\nany plans for today? i was hoping i could come over and trek out, i saw that\ntodays the 25th anniversary of the airing of your favorite episode and\nthought you might want to do something for that :)\nlet me know!\n\nmichael", True, (0, 0, 0))
john_mail_3_rect = john_mail_3.get_rect()
john_mail_3_rect.topleft = (420, 270)

john_mail_4_label = body_text.render("<nicolecat@mail.com> Birthday Surprise!! Aug 27 93", True, (0, 0, 0))
john_mail_4_label_rect = john_mail_4_label.get_rect()
john_mail_4_label_rect.topleft = (430, 432)

john_mail_4 = body_text.render("From <nicolecat@mail.com>: Birthday Surprise!!\n\nHi, John!\n\nI don't know if Michael's told you or not, but I'm studying abroad in\nGreece for the summer, so I'm going to miss Michael's birthday next\nweek! I remember Michael saying you're really good with computers;\ndo you know if it's possible to make a bunch of recordings play for him\nthroughout the day? I'm aiming for charming at first and really annoying by\nthe end :)\n\nNicole", True, (0, 0, 0))
john_mail_4_rect = john_mail_4.get_rect()
john_mail_4_rect.topleft = (420, 270)

john_mail_5_label = body_text.render("<desmondc@mail.com> RE:Thinking Machine? Dec 3 93", True, (0, 0, 0))
john_mail_5_label_rect = john_mail_5_label.get_rect()
john_mail_5_label_rect.topleft = (430, 482)

john_mail_5 = body_text.render("From <desmondc@mail.com>: RE:Thinking Machine?\n\nHello, John.\n\nI'm sorry, correct me if I'm wrong - you're saying that you're not sure,\nbut you ~think~ that you've developed an artificial personality\nsimulation? If that were true it would be the greatest discovery in\nthe field since its creation, but... please take no offense, it just\ndoesn't sound plausible that someone in your condition would have been\nable to. Do you have any proof you didn't just imagine the ordeal?\n\nDesmond Creed", True, (0, 0, 0))
john_mail_5_rect = john_mail_5.get_rect()
john_mail_5_rect.topleft = (420, 270)

john_mail_6_label = body_text.render("<michael&jello@mail.com> hey uncle john Mar 24 99", True, (0, 0, 0))
john_mail_6_label_rect = john_mail_6_label.get_rect()
john_mail_6_label_rect.topleft = (430, 532)

john_mail_6 = body_text.render("From <michael&jello@mail.com>: hey uncle john\n\ndo you remember me?\n\nits ok if you dont. im not going to be here much longer.\n\ni miss you\n\n-michael <3", True, (0, 0, 0))
john_mail_6_rect = john_mail_6.get_rect()
john_mail_6_rect.topleft = (420, 270)


hint_prompt = body_text.render("Need a hint?", True, (255, 255, 255))
hint_prompt_rect = password_prompt.get_rect()
hint_prompt_rect.center = (650, 585)

clock_block = body_text.render("Admin priveleges needed to change system time", True, (255, 255, 255))
clock_block_rect = clock_block.get_rect()
clock_block_rect.center = (800, 680)
clock_block.set_alpha(0)
screen.blit(clock_block, clock_block_rect)

finale = header.render("Current Time:\n\n", True, '#FFFFFF')
finale_rect = finale.get_rect()
finale_rect.midtop = (622, 100)

password_input_rect = pygame.Rect((625, 540), (250, 30))

current_time = datetime.datetime.now()
init_second = int(current_time.strftime("%S"))
init_minute = int(current_time.strftime("%M"))
init_hour = int(current_time.strftime("%I"))
init_meridian = current_time.strftime("%p")

second = (60 + int(current_time.strftime("%S")) - init_second) % 60
minute = ((63 + int(current_time.strftime("%M")) - init_minute) % 60)
hour = ((23 + int(current_time.strftime("%I")) - init_hour) % 12)
meridian = current_time.strftime("%p")
date = "December 31, "
year = "99, "

clock_display = body_text.render(
    "December 31, 99, AA "
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
clock_display_rect.center = (800, 715)


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

        if computer_on == False:
            screen.fill("#302732")
            screen.blit(outside, (0, 0))
            screen.blit(arm, pygame.mouse.get_pos())

        # On button
        if power_hitbox.collidepoint(point) and mouse_left and dummy >= 10:
            dummy = 0
            cursor_x = pygame.mouse.get_pos()[0]
            cursor_y = pygame.mouse.get_pos()[1]
            pygame.mixer.Sound.play(braammmm)
            
            screen.blit(outside, (0, 0))
            screen.blit(arm, (cursor_x - 5, cursor_y - 5))
            pygame.display.flip()
            pygame.time.delay(200)
            screen.blit(outside, (0, 0))
            screen.blit(arm, (cursor_x, cursor_y))
            pygame.display.flip()
            
            for i in range(15):
                pygame.time.delay(20)
                cursor_x += 5
                cursor_y += 10
                screen.blit(outside, (0, 0))
                screen.blit(arm, (cursor_x, cursor_y ))
                pygame.display.flip()

            pygame.time.delay(900)
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
            pygame.mouse.set_pos(622, 450)
            pygame.mouse.set_visible(True)
            screen.blit(login_prompt, login_prompt_rect)

        if computer_on == True and account == "no one":

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
                        if nicole_password == "":
                            nicole_password = password_input
                            account = "nicole"
                            pygame.time.delay(900)
                            screen.blit(backdrop,(276,165))
                        else:
                            if password_input == nicole_password:
                                account = "nicole"
                                pygame.time.delay(900)
                                screen.blit(backdrop,(276,165))
                    if (account_selected == "michael" and password_input == "kegsmasher1999"):
                        account = "michael"
                        pygame.time.delay(900)
                        screen.blit(backdrop,(276,165))
                    if account_selected == "john" and password_input == "M00nlander":
                        account = "john"
                        pygame.time.delay(900)
                        screen.blit(backdrop,(276,165))
                    if account_selected == "marion" and password_input == "I, Mudd":
                        account = "marion"
                        pygame.time.delay(900)
                        screen.blit(backdrop,(276,165))

                    if account != "no one":

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
                            mail_icon_hitbox = pygame.Rect((648, 470), (75, 95))
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
                        dummy = 0
                    )
                if account_selected == "michael":
                    hint_prompt = body_text.render(
                        "Need a hint?\ngreatest accomplishment + grad year",
                        True,
                        (255, 255, 255),
                        dummy = 0
                    )
                if account_selected == "john":
                    hint_prompt = body_text.render("Need a hint?\nMcD0nald's astr0naut", True, (255, 255, 255))
                    dummy = 0
                if account_selected == "marion":
                    hint_prompt = body_text.render("Need a hint?\n1011 11 11110101111", True, (255, 255, 255))
                    dummy = 0
                if mouse_left and not hint_prompt_rect.collidepoint(point) and dummy >= 0:
                    hint_prompt = body_text.render(
                        "Need a hint?", True, (255, 255, 255)
                    )
                    hint = False

        if account != "no one":

            if clock_display_rect.collidepoint(point) and mouse_left and dummy >= 10:
                dummy = 0
                if account == "marion":
                    pygame.time.delay(100)
                    game_over = True
                    were_in_the_endframe_now = 0
                else:
                    for i in range(255,0,-1):
                        clock_block.set_alpha(i)
                        # The best way I could figure out how to do this is to chop off each side of the backdrop image
                        screen.blit(backdrop.subsurface((671-276, 673-165), (259, 15)), clock_block_rect)
                        screen.blit(clock_block, clock_block_rect)
                        pygame.display.flip()
                        pygame.time.delay(10)

            if logout_hitbox.collidepoint(point) and mouse_left:
                account = "no one"
                account_selected = "no one"
                mail_open = False
                reading_mail = False
                music_open = False
                notes_open = False
                reading_notes = False
                photos_open = False
                pygame.time.delay(900)
                screen.blit(login_screen, (276, 165))
                screen.blit(login_prompt, login_prompt_rect)
                screen.blit(outside, (0, 0))


            if (mail_open == False and music_open == False and notes_open == False and photos_open == False and mail_icon_hitbox.collidepoint(point) and mouse_left and dummy >= 10) or (reading_mail == True and back_hitbox.collidepoint(point) and mouse_left and dummy >= 10):
                mail_open = True
                reading_mail = False
                dummy = 0
                screen.blit(mail_UI, (400, 200))
                pygame.draw.rect(screen, "white", mail_1_hitbox)
                pygame.draw.rect(screen, "white", mail_2_hitbox)
                pygame.draw.rect(screen, "white", mail_3_hitbox)
                pygame.draw.rect(screen, "white", mail_4_hitbox)
                pygame.draw.rect(screen, "white", mail_5_hitbox)
                pygame.draw.rect(screen, "white", mail_6_hitbox)
                if account == "nicole":
                    screen.blit(nicole_mail_1_label, nicole_mail_1_label_rect)
                    screen.blit(nicole_mail_2_label, nicole_mail_2_label_rect)
                    screen.blit(nicole_mail_3_label, nicole_mail_3_label_rect)
                    screen.blit(nicole_mail_4_label, nicole_mail_4_label_rect)
                    screen.blit(nicole_mail_5_label, nicole_mail_5_label_rect)
                    screen.blit(nicole_mail_6_label, nicole_mail_6_label_rect)
                if account == "michael":
                    screen.blit(michael_mail_1_label, michael_mail_1_label_rect)
                    screen.blit(michael_mail_2_label, michael_mail_2_label_rect)
                    screen.blit(michael_mail_3_label, michael_mail_3_label_rect)
                    screen.blit(michael_mail_4_label, michael_mail_4_label_rect)
                    screen.blit(michael_mail_5_label, michael_mail_5_label_rect)
                    screen.blit(michael_mail_6_label, michael_mail_6_label_rect)
                if account == "john":
                    screen.blit(john_mail_1_label, john_mail_1_label_rect)
                    screen.blit(john_mail_2_label, john_mail_2_label_rect)
                    screen.blit(john_mail_3_label, john_mail_3_label_rect)
                    screen.blit(john_mail_4_label, john_mail_4_label_rect)
                    screen.blit(john_mail_5_label, john_mail_5_label_rect)
                    screen.blit(john_mail_6_label, john_mail_6_label_rect)

            if mail_open == False and music_open == False and notes_open == False and photos_open == False and music_icon_hitbox.collidepoint(point) and mouse_left:
                music_open = True
                dummy = 0
                if pygame.mixer.music.get_busy() == False:
                    screen.blit(music_paused_UI, (400, 200))
                else:
                    screen.blit(music_playing_UI, (400, 200))

            if (mail_open == False and music_open == False and notes_open == False and photos_open == False and notes_icon_hitbox.collidepoint(point) and mouse_left) or (reading_notes == True and back_hitbox.collidepoint(point) and mouse_left and dummy >= 10):
                notes_open = True
                reading_notes = False
                dummy = 0
                screen.blit(notes_UI, (400, 200))
                pygame.draw.rect(screen, "white", note_1_hitbox)
                pygame.draw.rect(screen, "white", note_2_hitbox)
                pygame.draw.rect(screen, "white", note_3_hitbox)
                pygame.draw.rect(screen, "white", note_4_hitbox)
                pygame.draw.rect(screen, "white", note_5_hitbox)
                pygame.draw.rect(screen, "white", note_6_hitbox)
                
                if account == "nicole":
                    screen.blit(nicole_note_1_date, nicole_note_1_date_rect)
                    screen.blit(nicole_note_2_date, nicole_note_2_date_rect)
                    screen.blit(nicole_note_3_date, nicole_note_3_date_rect)
                    screen.blit(nicole_note_4_date, nicole_note_4_date_rect)
                    screen.blit(nicole_note_5_date, nicole_note_5_date_rect)
                    screen.blit(nicole_note_6_date, nicole_note_6_date_rect)
                if account == "michael":
                    screen.blit(michael_note_1_date, michael_note_1_date_rect)
                    screen.blit(michael_note_2_date, michael_note_2_date_rect)
                    screen.blit(michael_note_3_date, michael_note_3_date_rect)
                    screen.blit(michael_note_4_date, michael_note_4_date_rect)
                    screen.blit(michael_note_5_date, michael_note_5_date_rect)
                    screen.blit(michael_note_6_date, michael_note_6_date_rect)
                if account == "john":
                    screen.blit(john_note_1_date, john_note_1_date_rect)
                    screen.blit(john_note_2_date, john_note_2_date_rect)
                    screen.blit(john_note_3_date, john_note_3_date_rect)
                    screen.blit(john_note_4_date, john_note_4_date_rect)
                    screen.blit(john_note_5_date, john_note_5_date_rect)
                    screen.blit(john_note_6_date, john_note_6_date_rect)
                if account == "marion":
                    screen.blit(marion_note_1_date, marion_note_1_date_rect)
                    screen.blit(marion_note_2_date, marion_note_2_date_rect)
                    screen.blit(marion_note_3_date, marion_note_3_date_rect)
                    screen.blit(marion_note_4_date, marion_note_4_date_rect)
                    screen.blit(marion_note_5_date, marion_note_5_date_rect)
                    screen.blit(marion_note_6_date, marion_note_6_date_rect)                

            if mail_open == False and music_open == False and notes_open == False and photos_open == False and photos_icon_hitbox.collidepoint(point) and mouse_left:
                photos_open = True
                photo = 1
                screen.blit(photos_UI, (400, 200))
                if account == "nicole":
                    screen.blit(nicole_photo_1, (480, 265))
                if account == "michael":
                    screen.blit(michael_photo_1, (480, 265))
                if account == "john":
                    screen.blit(john_photo_1, (480, 265))
            
            if mail_open == True and dummy >= 10:
                if reading_mail == False:
                    if mail_1_hitbox.collidepoint(point) or mail_2_hitbox.collidepoint(point) or mail_3_hitbox.collidepoint(point) or mail_4_hitbox.collidepoint(point) or mail_5_hitbox.collidepoint(point) or mail_6_hitbox.collidepoint(point) and mouse_left:
                        pygame.draw.rect(screen, "white", ((410, 260), (440, 310)))
                        screen.blit(mail_back, back_hitbox)
                        reading_mail = True
                        dummy = 0

                        if account == "nicole" and mail_1_hitbox.collidepoint(point):
                            screen.blit(nicole_mail_1, nicole_mail_1_rect)
                        if account == "nicole" and mail_2_hitbox.collidepoint(point):
                            screen.blit(nicole_mail_2, nicole_mail_2_rect)
                        if account == "nicole" and mail_3_hitbox.collidepoint(point):
                            screen.blit(nicole_mail_3, nicole_mail_3_rect)
                        if account == "nicole" and mail_4_hitbox.collidepoint(point):
                            screen.blit(nicole_mail_4, nicole_mail_4_rect)
                        if account == "nicole" and mail_5_hitbox.collidepoint(point):
                            screen.blit(nicole_mail_5, nicole_mail_5_rect)
                        if account == "nicole" and mail_6_hitbox.collidepoint(point):
                            screen.blit(nicole_mail_6, nicole_mail_6_rect)

                        if account == "michael" and mail_1_hitbox.collidepoint(point):
                            screen.blit(michael_mail_1, michael_mail_1_rect)
                        if account == "michael" and mail_2_hitbox.collidepoint(point):
                            screen.blit(michael_mail_2, michael_mail_2_rect)
                        if account == "michael" and mail_3_hitbox.collidepoint(point):
                            screen.blit(michael_mail_3, michael_mail_3_rect)
                        if account == "michael" and mail_4_hitbox.collidepoint(point):
                            screen.blit(michael_mail_4, michael_mail_4_rect)
                        if account == "michael" and mail_5_hitbox.collidepoint(point):
                            screen.blit(michael_mail_5, michael_mail_5_rect)
                        if account == "michael" and mail_6_hitbox.collidepoint(point):
                            screen.blit(michael_mail_6, michael_mail_6_rect)

                        if account == "john" and mail_1_hitbox.collidepoint(point):
                            screen.blit(john_mail_1, john_mail_1_rect)
                        if account == "john" and mail_2_hitbox.collidepoint(point):
                            screen.blit(john_mail_2, john_mail_2_rect)
                        if account == "john" and mail_3_hitbox.collidepoint(point):
                            screen.blit(john_mail_3, john_mail_3_rect)
                        if account == "john" and mail_4_hitbox.collidepoint(point):
                            screen.blit(john_mail_4, john_mail_4_rect)
                        if account == "john" and mail_5_hitbox.collidepoint(point):
                            screen.blit(john_mail_5, john_mail_5_rect)
                        if account == "john" and mail_6_hitbox.collidepoint(point):
                            screen.blit(john_mail_6, john_mail_6_rect)
            
            if music_open == True:
                if music_play_hitbox.collidepoint(point) and mouse_left and dummy >= 10:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                        screen.blit(music_paused_UI, (400, 200))
                        dummy = 0
                    else:
                        pygame.mixer.music.unpause()
                        screen.blit(music_playing_UI, (400, 200))
                        dummy = 0
            
            if notes_open == True and dummy >= 10:
                if reading_notes == False:
                    if note_1_hitbox.collidepoint(point) or note_2_hitbox.collidepoint(point) or note_3_hitbox.collidepoint(point) or note_4_hitbox.collidepoint(point) or note_5_hitbox.collidepoint(point) or note_6_hitbox.collidepoint(point) and mouse_left:
                        pygame.draw.rect(screen, "white", ((410, 260), (440, 310)))
                        screen.blit(notes_back, back_hitbox)
                        reading_notes = True
                        dummy = 0

                        if account == "nicole" and note_1_hitbox.collidepoint(point):
                            screen.blit(nicole_note_1, nicole_note_1_rect)
                        if account == "nicole" and note_2_hitbox.collidepoint(point):
                            screen.blit(nicole_note_2, nicole_note_2_rect)
                        if account == "nicole" and note_3_hitbox.collidepoint(point):
                            screen.blit(nicole_note_3, nicole_note_3_rect)
                        if account == "nicole" and note_4_hitbox.collidepoint(point):
                            screen.blit(nicole_note_4, nicole_note_4_rect)
                        if account == "nicole" and note_5_hitbox.collidepoint(point):
                            screen.blit(nicole_note_5, nicole_note_5_rect)
                        if account == "nicole" and note_6_hitbox.collidepoint(point):
                            screen.blit(nicole_note_6, nicole_note_6_rect)
                        
                        if account == "michael" and note_1_hitbox.collidepoint(point):
                            screen.blit(michael_note_1, michael_note_1_rect)
                        if account == "michael" and note_2_hitbox.collidepoint(point):
                            screen.blit(michael_note_2, michael_note_2_rect)
                        if account == "michael" and note_3_hitbox.collidepoint(point):
                            screen.blit(michael_note_3, michael_note_3_rect)
                        if account == "michael" and note_4_hitbox.collidepoint(point):
                            screen.blit(michael_note_4, michael_note_4_rect)
                        if account == "michael" and note_5_hitbox.collidepoint(point):
                            screen.blit(michael_note_5, michael_note_5_rect)
                        if account == "michael" and note_6_hitbox.collidepoint(point):
                            screen.blit(michael_note_6, michael_note_6_rect)
                            
                        if account == "john" and note_1_hitbox.collidepoint(point):
                            screen.blit(john_note_1, john_note_1_rect)
                        if account == "john" and note_2_hitbox.collidepoint(point):
                            screen.blit(john_note_2, john_note_2_rect)
                        if account == "john" and note_3_hitbox.collidepoint(point):
                            screen.blit(john_note_3, john_note_3_rect)
                        if account == "john" and note_4_hitbox.collidepoint(point):
                            screen.blit(john_note_4, john_note_4_rect)
                        if account == "john" and note_5_hitbox.collidepoint(point):
                            screen.blit(john_note_5, john_note_5_rect)
                        if account == "john" and note_6_hitbox.collidepoint(point):
                            screen.blit(john_note_6, john_note_6_rect)
                            
                        if account == "marion" and note_1_hitbox.collidepoint(point):
                            screen.blit(marion_note_1, marion_note_1_rect)
                        if account == "marion" and note_2_hitbox.collidepoint(point):
                            screen.blit(marion_note_2, marion_note_2_rect)
                        if account == "marion" and note_3_hitbox.collidepoint(point):
                            screen.blit(marion_note_3, marion_note_3_rect)
                        if account == "marion" and note_4_hitbox.collidepoint(point):
                            screen.blit(marion_note_4, marion_note_4_rect)
                        if account == "marion" and note_5_hitbox.collidepoint(point):
                            screen.blit(marion_note_5, marion_note_5_rect)
                        if account == "marion" and note_6_hitbox.collidepoint(point):
                            screen.blit(marion_note_6, marion_note_6_rect)


            if photos_open == True:

                if photos_left_hitbox.collidepoint(point) and mouse_left and dummy >= 10:
                    if photo == 1 and dummy >= 10:
                        if account == "nicole":
                            screen.blit(nicole_photo_3, (480, 265))
                            photo = 3
                            dummy = 0
                        if account == "michael":
                            screen.blit(michael_photo_3, (480, 265))
                            photo = 3
                            dummy = 0
                        if account == "john":
                            screen.blit(john_photo_3, (480, 265))
                            photo = 3
                            dummy = 0
                    if photo == 2:
                        if account == "nicole" and dummy >= 10:
                            screen.blit(nicole_photo_1, (480, 265))
                            photo = 1
                            dummy = 0
                        if account == "michael" and dummy >= 10:
                            screen.blit(michael_photo_1, (480, 265))
                            photo = 1
                            dummy = 0
                        if account == "john" and dummy >= 10:
                            screen.blit(john_photo_1, (480, 265))
                            photo = 1
                            dummy = 0
                    if photo == 3:
                        if account == "nicole" and dummy >= 10:
                            screen.blit(nicole_photo_2, (480, 265))
                            photo = 2 
                            dummy = 0
                        if account == "michael" and dummy >= 10:
                            screen.blit(michael_photo_2, (480, 265))
                            photo = 2
                            dummy = 0
                        if account == "john" and dummy >= 10:
                            screen.blit(john_photo_2, (480, 265))
                            photo = 2
                            dummy = 0

                if photos_right_hitbox.collidepoint(point) and mouse_left and dummy >= 10:
                    if photo == 2 and dummy >= 10:
                        if account == "nicole" and dummy >= 10:
                            screen.blit(nicole_photo_3, (480, 265))
                            photo = 3
                            dummy = 0
                        if account == "michael" and dummy >= 10:
                            screen.blit(michael_photo_3, (480, 265))
                            photo = 3
                            dummy = 0
                        if account == "john" and dummy >= 10:
                            screen.blit(john_photo_3, (480, 265))
                            photo = 3
                            dummy = 0
                    if photo == 3:
                        if account == "nicole" and dummy >= 10:
                            screen.blit(nicole_photo_1, (480, 265))
                            photo = 1
                            dummy = 0
                        if account == "michael" and dummy >= 10:
                            screen.blit(michael_photo_1, (480, 265))
                            photo = 1
                            dummy = 0
                        if account == "john" and dummy >= 10:
                            screen.blit(john_photo_1, (480, 265))
                            photo = 1
                            dummy = 0
                    if photo == 1:
                        if account == "nicole" and dummy >= 10:
                            screen.blit(nicole_photo_2, (480, 265))
                            photo = 2 
                            dummy = 0
                        if account == "michael" and dummy >= 10:
                            screen.blit(michael_photo_2, (480, 265))
                            photo = 2
                            dummy = 0
                        if account == "john" and dummy >= 10:
                            screen.blit(john_photo_2, (480, 265))
                            photo = 2
                            dummy = 0


            if UI_Exit_hitbox.collidepoint(point) and mouse_left:
                mail_open = False
                reading_mail = False
                music_open = False
                notes_open = False
                reading_notes = False
                photos_open = False
                screen.blit(backdrop,(276,165))

                if account == "nicole":
                    screen.blit(music_icon, (498, 320))
                    music_icon_hitbox = pygame.Rect((498, 320), (75, 95))
                    screen.blit(notes_icon, (648, 320))
                    notes_icon_hitbox = pygame.Rect((648, 320), (75, 95))
                    screen.blit(photos_icon, (498, 470))
                    photos_icon_hitbox = pygame.Rect((498, 470), (75, 95))
                    screen.blit(mail_icon, (648, 470))
                    mail_icon_hitbox = pygame.Rect((648, 470), (75, 95))
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
                pygame.draw.rect(screen, (230, 235, 240), (277, 700, 690, 35))
                screen.blit(clock_display, clock_display_rect)
                screen.blit(logout_icon, (285, 665))
                screen.blit(outside,(0,0))


    if not mouse_left and dummy <= 10:
        dummy += 1

    current_time = datetime.datetime.now()
    second = int(current_time.strftime("%S"))
    if second < 10:
        second = "0" + str(second)
    minute = ((63 + int(current_time.strftime("%M")) - init_minute) % 60)
    if minute < 10:
        minute = "0" + str(minute)
    hour = ((23 + int(current_time.strftime("%I")) - init_hour) % 12)
    if int(hour) > 11:
        if game_over == False:
            date = "January 1, "
        meridian = "AM"
        clock_text = (
            date + year
            + str(hour)
            + ":"
            + str(minute)
            + ":"
            + str(second)
            + " "
            + meridian
            )
        clock_display = body_text.render(clock_text, True, (0, 0, 0))
    else:
        date = "December 31, "
        meridian = "PM"
        clock_text = (
            str(date) + str(year)
            + str(hour)
            + ":"
            + str(minute)
            + ":"
            + str(second)
            + " "
            + meridian
            )
        clock_display = body_text.render(clock_text, True, (0, 0, 0))
    if account != "no one" and game_over == False:
        pygame.draw.rect(screen, (230, 235, 240), clock_display_rect)
        screen.blit(clock_display, clock_display_rect)

    if game_over == True:

        if were_in_the_endframe_now == 1:
            finale = header.render("                Current Time:\n\n" + clock_text, True, '#FFFFFF')
            finale_rect = finale.get_rect()
            finale_rect.center = (622, 450)
        
        if were_in_the_endframe_now <= 10*60:
            pygame.mixer.stop()
            pygame.mixer.music.stop()
            if were_in_the_endframe_now >= 5*60:
                year = "89, "
                clock_text = (str(date) + str(year) + str(hour) + ":" + str(minute) + ":" + str(second) + " " + meridian)
            pygame.draw.rect(screen, '#000000', ((0, 0), (1244, 900)))
            finale = header.render("                Current Time:\n\n" + clock_text, True, '#FFFFFF')
            if were_in_the_endframe_now >= 4*60 and were_in_the_endframe_now < 5*60:
                pygame.draw.rect(screen, '#FFFFFF', ((615, 459), (12, 19)))
            if were_in_the_endframe_now <= 8*60:
                screen.blit(finale, finale_rect)
        
        if were_in_the_endframe_now == 10*60:
            pygame.mixer.Sound.play(fireworks)            
            pygame.mixer.music.load("Assets/Audio Assets/moremusic.mp3")
            pygame.mixer.music.play(-1)
        
        if were_in_the_endframe_now > 10*60:
            if were_in_the_endframe_now <= 13*60:
                finale = header.render("  Thank you\nfor playing :)", True, '#FFFFFF')
                finale_rect = finale.get_rect()
                finale_rect.center = (622, 450)
                pygame.draw.rect(screen, '#000000', ((0, 0), (1244, 900)))
                screen.blit(finale, finale_rect)
            if were_in_the_endframe_now > 13*60 and were_in_the_endframe_now < 15*60:
                pygame.draw.rect(screen, '#000000', ((0, 0), (1244, 900)))
            if were_in_the_endframe_now >= 15*60:
                finale = header.render("Credits", True, '#FFFFFF')
                finale_rect = finale.get_rect()
                finale_rect.midtop = (622, 300)
                pygame.draw.rect(screen, '#000000', ((0, 0), (1244, 900)))
                screen.blit(finale, finale_rect)
                finale = header.render("Concept         Ivy Edwards, Devin Gulliver, Kate Korb\n\nCode              Ivy Edwards, Kate Korb\n\nMusic             Devin Gulliver\n\nStory             Ivy Edwards\n\nArt                Ivy Edwards\n\nPlaying          You :)", True, '#FFFFFF')
                finale_rect = finale.get_rect()
                finale_rect.center = (622, 450)
                screen.blit(finale, finale_rect)
        were_in_the_endframe_now += 1

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()