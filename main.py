import pygame
from sys import exit
import datetime
from settings import *

pygame.init()
pygame.mixer.init()


def text_button(box, text, rect, colour = 'gray'):
    pygame.draw.rect(screen, colour, box,  2, 100 )
    if box.collidepoint(mouse_pos):
        pygame.draw.rect(screen, colour, pygame.Rect(rect.topleft[0] - (text.get_size()[0] // 4), rect.topleft[1] - (text.get_size()[1] // 4), text.get_size()[0] * 1.5, text.get_size()[1] * 1.5), 0, 100 )
        screen.blit(text, rect)
        if clicking:
            return True
    screen.blit(text, rect)

def pause_button(bool, box, text, rect, colour = "gray"):
    if bool == False:
        text = text_font.render('Pause', True, TEXT_COLOUR)
        rect = esad_gaming_pause_text.get_rect()
        rect.center = (WIDTH // 2, HEIGHT // 10 * 6)
        box = pygame.Rect(rect.topleft[0] - (text.get_size()[0] // 4), rect.topleft[1] - (text.get_size()[1] // 4), text.get_size()[0] * 1.5, text.get_size()[1] * 1.5)
    else:
        text = text_font.render('Unpause', True, TEXT_COLOUR)
        rect = esad_gaming_pause_text.get_rect()
        rect.center = (WIDTH // 2, HEIGHT // 10 * 7)
        box = pygame.Rect(rect.topleft[0] - (text.get_size()[0] // 4), rect.topleft[1] - (text.get_size()[1] // 4), text.get_size()[0] * 1.5, text.get_size()[1] * 1.5)
    screen.blit(text, rect)

    pygame.draw.rect(screen, colour, box,  2, 100 )
    if box.collidepoint(mouse_pos):
        pygame.draw.rect(screen, colour, pygame.Rect(rect.topleft[0] - (text.get_size()[0] // 4), rect.topleft[1] - (text.get_size()[1] // 4), text.get_size()[0] * 1.5, text.get_size()[1] * 1.5), 0, 100 )
        if clicking and bool == False:
            return True
        elif clicking and bool == True:
            return False
        elif clicking == False and bool == False:
            return False
        elif clicking == False and bool == True:
            return True

screen = pygame.display.set_mode(RES)
pygame.display.set_caption('Süre Manager')
clock = pygame.time.Clock()
running = True
title_font = pygame.font.Font(FONT, TITLE_FONT_SIZE)
text_font = pygame.font.Font(FONT, TEXT_FONT_SIZE)

clicking = False

# Title
title_text = title_font.render('Süre Manager', True, TEXT_COLOUR)
title_text_rect = title_text.get_rect()
title_text_rect.center = (WIDTH // 2, HEIGHT // 8)

pygame.mixer.music.load('sounds/alarm.wav')
pygame.mixer.music.set_volume(1)


# OPTIONS
    # Esad
esad_text = text_font.render('Esad', True, TEXT_COLOUR)
esad_text_rect = esad_text.get_rect()
esad_text_rect.center = (WIDTH // 4, HEIGHT // 2)
esad_text_box = pygame.Rect(esad_text_rect.topleft[0] - (esad_text.get_size()[0] // 4), esad_text_rect.topleft[1] - (esad_text.get_size()[1] // 4), esad_text.get_size()[0] * 1.5, esad_text.get_size()[1] * 1.5)
esad = False
    # Etka
etka_text = text_font.render('Serhat', True, TEXT_COLOUR)
etka_text_rect = etka_text.get_rect()
etka_text_rect.center = (WIDTH - (WIDTH // 4), HEIGHT // 2)
etka_text_box = pygame.Rect(etka_text_rect.topleft[0] - (etka_text.get_size()[0] // 4), etka_text_rect.topleft[1] - (etka_text.get_size()[1] // 4), etka_text.get_size()[0] * 1.5, etka_text.get_size()[1] * 1.5)
etka = False


# Options Menus
# Esad Time
if datetime.date.today().weekday() in list(range(0, 3)):
    esad_gaming_hours = 0
    esad_gaming_minutes = 45
    esad_gaming_seconds = 0
else:
    esad_gaming_hours = 2
    esad_gaming_minutes = 30
    esad_gaming_seconds = 0

if datetime.date.today().weekday() in list(range(0, 3)):
    esad_coding_hours = 0
    esad_coding_minutes = 45
    esad_coding_seconds = 0
else:
    esad_coding_hours = 1
    esad_coding_minutes = 0
    esad_coding_seconds = 0

# Etka Time
if datetime.date.today().weekday() in list(range(0, 3)):
    etka_gaming_hours = 0
    etka_gaming_minutes = 30
    etka_gaming_seconds = 0
else:
    etka_gaming_hours = 2
    etka_gaming_minutes = 30
    etka_gaming_seconds = 0

if datetime.date.today().weekday() in list(range(0, 3)):
    etka_coding_hours = 0
    etka_coding_minutes = 15
    etka_coding_seconds = 0
else:
    etka_coding_hours = 1
    etka_coding_minutes = 0
    etka_coding_seconds = 0

    # ESAD MENU
esad_menu_gaming_text = text_font.render(f'Start gaming timer ({esad_gaming_hours}h {esad_gaming_minutes}m)', True, TEXT_COLOUR)
esad_menu_gaming_text_rect = esad_menu_gaming_text.get_rect()
esad_menu_gaming_text_rect.center = (WIDTH // 2, HEIGHT // 2.5)
esad_menu_gaming_text_box = pygame.Rect(esad_menu_gaming_text_rect.topleft[0] - (esad_menu_gaming_text.get_size()[0] // 4), esad_menu_gaming_text_rect.topleft[1] - (esad_menu_gaming_text.get_size()[1] // 4), esad_menu_gaming_text.get_size()[0] * 1.5, esad_menu_gaming_text.get_size()[1] * 1.5)
esad_menu_gaming = False

esad_menu_coding_text = text_font.render(f'Start coding timer ({esad_coding_hours}h {esad_coding_minutes}m)', True, TEXT_COLOUR)
esad_menu_coding_text_rect = esad_menu_coding_text.get_rect()
esad_menu_coding_text_rect.center = (WIDTH // 2, HEIGHT // 1.5)
esad_menu_coding_text_box = pygame.Rect(esad_menu_coding_text_rect.topleft[0] - (esad_menu_coding_text.get_size()[0] // 4), esad_menu_coding_text_rect.topleft[1] - (esad_menu_coding_text.get_size()[1] // 4), esad_menu_coding_text.get_size()[0] * 1.5, esad_menu_coding_text.get_size()[1] * 1.5)
esad_menu_coding = False
    # ETKA MENU
etka_menu_gaming_text = text_font.render(f'Start gaming timer ({etka_gaming_hours}h {etka_gaming_minutes}m)', True, TEXT_COLOUR)
etka_menu_gaming_text_rect = etka_menu_gaming_text.get_rect()
etka_menu_gaming_text_rect.center = (WIDTH // 2, HEIGHT // 2.5)
etka_menu_gaming_text_box = pygame.Rect(etka_menu_gaming_text_rect.topleft[0] - (etka_menu_gaming_text.get_size()[0] // 4), etka_menu_gaming_text_rect.topleft[1] - (etka_menu_gaming_text.get_size()[1] // 4), etka_menu_gaming_text.get_size()[0] * 1.5, etka_menu_gaming_text.get_size()[1] * 1.5)
etka_menu_gaming = False

etka_menu_coding_text = text_font.render(f'Start coding timer ({etka_coding_hours}h {etka_coding_minutes}m)', True, TEXT_COLOUR)
etka_menu_coding_text_rect = etka_menu_coding_text.get_rect()
etka_menu_coding_text_rect.center = (WIDTH // 2, HEIGHT // 1.5)
etka_menu_coding_text_box = pygame.Rect(etka_menu_coding_text_rect.topleft[0] - (etka_menu_coding_text.get_size()[0] // 4), etka_menu_coding_text_rect.topleft[1] - (etka_menu_coding_text.get_size()[1] // 4), etka_menu_coding_text.get_size()[0] * 1.5, etka_menu_coding_text.get_size()[1] * 1.5)
etka_menu_coding = False


# Timers
    # Esad Gaming
esad_gaming_text = title_font.render('Esad gaming Timer', True, TEXT_COLOUR)
esad_gaming_text_rect = esad_gaming_text.get_rect()
esad_gaming_text_rect.center = (WIDTH // 2, HEIGHT // 8)
esad_gaming_time = esad_gaming_hours * 3600 + esad_gaming_minutes * 60 + esad_gaming_seconds    # h * 3600 + m * 60, s
esad_gaming_time_text = text_font.render('loading...', True, TEXT_COLOUR)
esad_gaming_time_text_rect = esad_gaming_time_text.get_rect()
esad_gaming_time_text_rect.center = (WIDTH // 2, HEIGHT // 2)

esad_gaming_paused = False
esad_gaming_pause_text = text_font.render('Pause', True, TEXT_COLOUR)
esad_gaming_pause_text_rect = esad_gaming_pause_text.get_rect()
esad_gaming_pause_text_rect.center = (WIDTH // 2, HEIGHT // 5 * 3)
esad_gaming_pause_text_box = pygame.Rect(esad_gaming_pause_text_rect.topleft[0] - (esad_gaming_pause_text.get_size()[0] // 4), esad_gaming_pause_text_rect.topleft[1] - (esad_gaming_pause_text.get_size()[1] // 4), esad_gaming_pause_text.get_size()[0] * 1.5, esad_gaming_pause_text.get_size()[1] * 1.5)
    # Esad Coding
esad_coding_text = title_font.render('Esad coding Timer', True, TEXT_COLOUR)
esad_coding_text_rect = esad_coding_text.get_rect()
esad_coding_text_rect.center = (WIDTH // 2, HEIGHT // 8)
esad_coding_time = esad_coding_hours * 3600 + esad_coding_minutes * 60 + esad_coding_seconds    # h * 3600 + m * 60, s
esad_coding_time_text = text_font.render('loading...', True, TEXT_COLOUR)
esad_coding_time_text_rect = esad_coding_time_text.get_rect()
esad_coding_time_text_rect.center = (WIDTH // 2, HEIGHT // 2)

esad_coding_paused = False
esad_coding_pause_text = text_font.render('Pause', True, TEXT_COLOUR)
esad_coding_pause_text_rect = esad_coding_pause_text.get_rect()
esad_coding_pause_text_rect.center = (WIDTH // 2, HEIGHT // 5 * 3)
esad_coding_pause_text_box = pygame.Rect(esad_coding_pause_text_rect.topleft[0] - (esad_coding_pause_text.get_size()[0] // 4), esad_coding_pause_text_rect.topleft[1] - (esad_coding_pause_text.get_size()[1] // 4), esad_coding_pause_text.get_size()[0] * 1.5, esad_coding_pause_text.get_size()[1] * 1.5)
    # Etka Gaming
etka_gaming_text = title_font.render('Etka gaming Timer', True, TEXT_COLOUR)
etka_gaming_text_rect = etka_gaming_text.get_rect()
etka_gaming_text_rect.center = (WIDTH // 2, HEIGHT // 8)
etka_gaming_time = etka_gaming_hours * 3600 + etka_gaming_minutes * 60 + etka_gaming_seconds    # h * 3600 + m * 60, s
etka_gaming_time_text = text_font.render('loading...', True, TEXT_COLOUR)
etka_gaming_time_text_rect = etka_gaming_time_text.get_rect()
etka_gaming_time_text_rect.center = (WIDTH // 2, HEIGHT // 2)

etka_gaming_paused = False
etka_gaming_pause_text = text_font.render('Pause', True, TEXT_COLOUR)
etka_gaming_pause_text_rect = etka_gaming_pause_text.get_rect()
etka_gaming_pause_text_rect.center = (WIDTH // 2, HEIGHT // 5 * 3)
etka_gaming_pause_text_box = pygame.Rect(etka_gaming_pause_text_rect.topleft[0] - (etka_gaming_pause_text.get_size()[0] // 4), etka_gaming_pause_text_rect.topleft[1] - (etka_gaming_pause_text.get_size()[1] // 4), etka_gaming_pause_text.get_size()[0] * 1.5, etka_gaming_pause_text.get_size()[1] * 1.5)
    # Etka Coding
etka_coding_text = title_font.render('Etka coding Timer', True, TEXT_COLOUR)
etka_coding_text_rect = etka_coding_text.get_rect()
etka_coding_text_rect.center = (WIDTH // 2, HEIGHT // 8)
etka_coding_time = etka_coding_hours * 3600 + etka_coding_minutes * 60 + etka_coding_seconds    # h * 3600 + m * 60, s
etka_coding_time_text = text_font.render('loading...', True, TEXT_COLOUR)
etka_coding_time_text_rect = etka_coding_time_text.get_rect()
etka_coding_time_text_rect.center = (WIDTH // 2, HEIGHT // 2)

etka_coding_paused = False
etka_coding_pause_text = text_font.render('Pause', True, TEXT_COLOUR)
etka_coding_pause_text_rect = etka_coding_pause_text.get_rect()
etka_coding_pause_text_rect.center = (WIDTH // 2, HEIGHT // 5 * 3)
etka_coding_pause_text_box = pygame.Rect(etka_coding_pause_text_rect.topleft[0] - (etka_coding_pause_text.get_size()[0] // 4), etka_coding_pause_text_rect.topleft[1] - (etka_coding_pause_text.get_size()[1] // 4), etka_coding_pause_text.get_size()[0] * 1.5, etka_coding_pause_text.get_size()[1] * 1.5)

second_timer = 0
sound_played = False


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicking = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicking = False


    mouse_pos = pygame.mouse.get_pos()

    # Background
    screen.fill('white')

    # Title
    screen.blit(title_text, title_text_rect)

    # Options
    esad = text_button(esad_text_box, esad_text, esad_text_rect)
    etka = text_button(etka_text_box, etka_text, etka_text_rect)

    clock.tick(FPS)
    pygame.display.update()


    while esad:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esad = False
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicking = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicking = False


        mouse_pos = pygame.mouse.get_pos()

        # Background
        screen.fill('white')

        # Title
        screen.blit(title_text, title_text_rect)

        # Options
        esad_menu_gaming = text_button(esad_menu_gaming_text_box, esad_menu_gaming_text, esad_menu_gaming_text_rect)
        esad_menu_coding = text_button(esad_menu_coding_text_box, esad_menu_coding_text, esad_menu_coding_text_rect)

        if esad_menu_gaming:
            break
        elif esad_menu_coding:
            break


        clock.tick(FPS)
        pygame.display.update()


    while etka:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                etka = False
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicking = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicking = False


        mouse_pos = pygame.mouse.get_pos()

        # Background
        screen.fill('white')

        # Title
        screen.blit(title_text, title_text_rect)

        # Options
        etka_menu_gaming = text_button(etka_menu_gaming_text_box, etka_menu_gaming_text, etka_menu_gaming_text_rect)
        etka_menu_coding = text_button(etka_menu_coding_text_box, etka_menu_coding_text, etka_menu_coding_text_rect)

        if etka_menu_gaming:
            break
        elif etka_menu_coding:
            break


        clock.tick(FPS)
        pygame.display.update()

    
    while esad_menu_gaming:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esad_menu_gaming = False
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicking = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicking = False
        
        mouse_pos = pygame.mouse.get_pos()

        # Background
        screen.fill('white')


        # Title
        screen.blit(esad_gaming_text, esad_gaming_text_rect)

        esad_gaming_paused = pause_button(esad_gaming_paused, esad_gaming_pause_text_box, esad_gaming_pause_text, esad_gaming_pause_text_rect)
        print(esad_gaming_paused) # debug

        # Timer
        if esad_gaming_paused == False:
            second_timer += 1 / clock.get_fps()
            if second_timer >= 1:
                if esad_gaming_time > 0:
                    timer = datetime.timedelta(seconds = esad_gaming_time)
                    esad_gaming_time -= 1
                    second_timer = 0
                    esad_gaming_time_text = text_font.render(str(timer) , True, TEXT_COLOUR)
        screen.blit(esad_gaming_time_text, esad_gaming_time_text_rect)

        # Play timer sound
        if esad_gaming_time <= 0 and sound_played == False:
            pygame.mixer.music.play()
            sound_played = True


        clock.tick(FPS)
        pygame.display.update()


    while esad_menu_coding:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esad_menu_coding = False
                running = False
        

        # Background
        screen.fill('white')


        # Title
        screen.blit(esad_coding_text, esad_coding_text_rect)


        # Timer
        second_timer += 1 / clock.get_fps()
        if second_timer >= 1:
            if esad_coding_time > 0:
                timer = datetime.timedelta(seconds = esad_coding_time)
                esad_coding_time -= 1
                second_timer = 0
                esad_gaming_time_text = text_font.render(str(timer) , True, TEXT_COLOUR)
        screen.blit(esad_gaming_time_text, esad_gaming_time_text_rect)

        # Play timer sound
        if esad_coding_time <= 0:
            pygame.mixer.music.play()


        clock.tick(FPS)
        pygame.display.update()


    while etka_menu_gaming:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                etka_menu_gaming = False
                running = False
        

        # Background
        screen.fill('white')


        # Title
        screen.blit(etka_gaming_text, etka_gaming_text_rect)


        # Timer
        second_timer += 1 / clock.get_fps()
        if second_timer >= 1:
            if etka_gaming_time > 0:
                timer = datetime.timedelta(seconds = etka_gaming_time)
                etka_gaming_time -= 1
                second_timer = 0
                etka_gaming_time_text = text_font.render(str(timer) , True, TEXT_COLOUR)
        screen.blit(etka_gaming_time_text, etka_gaming_time_text_rect)

        # Play timer sound
        if etka_gaming_time <= 0:
            pygame.mixer.music.play()


        clock.tick(FPS)
        pygame.display.update()


    while etka_menu_coding:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                etka_menu_coding = False
                running = False
        

        # Background
        screen.fill('white')


        # Title
        screen.blit(etka_coding_text, etka_coding_text_rect)


        # Timer
        second_timer += 1 / clock.get_fps()
        if second_timer >= 1:
            if etka_coding_time > 0:
                timer = datetime.timedelta(seconds = etka_coding_time)
                etka_coding_time -= 1
                second_timer = 0
                etka_gaming_time_text = text_font.render(str(timer) , True, TEXT_COLOUR)
        screen.blit(etka_gaming_time_text, etka_gaming_time_text_rect)

        # Play timer sound
        if etka_coding_time <= 0:
            pygame.mixer.music.play()


        clock.tick(FPS)
        pygame.display.update()


pygame.quit()
exit()
