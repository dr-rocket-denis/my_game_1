import pygame
import random

pygame.init()

WIDTH, HEIGHT = 660, 440
FPS = 60

display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Убеги от злыдня')

hero = pygame.image.load('resources/hero.png')
fon = pygame.image.load('resources/fon.jpg')
start = pygame.image.load('resources/start.png')
start_color = pygame.image.load('resources/start_color1.png')

frame = 1
x = WIDTH // 2 - 72
x_pos_r = False
x_pos_l = False
speed_hero = 5
playing = False

play = True
while play:   
    pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x_pos_r = True
                x_pos_l = False
            elif event.key == pygame.K_LEFT:
                x_pos_r = False
                x_pos_l = True
            elif event.key == pygame.K_SPACE:
                playing = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_pos_r = False
            elif event.key == pygame.K_LEFT:
                x_pos_l = False
    if x_pos_r == True:
        x += speed_hero
    elif x_pos_l == True:
        x -= speed_hero
    frame = (frame + 0.1) % 3
    display.blit(fon, (0, 0))
    if playing == True:
        display.blit(hero, (x, 110), (144 * int(frame), 0, 144, 286))
    else:
        if mouse_pos[0] > 190 and mouse_pos[0] < 470 and mouse_pos[1] > 160 and mouse_pos[1] < 280:
            display.blit(start_color, (WIDTH//2-146, HEIGHT//2-64))
            if pressed[0]: 
                playing = True
        else:
            display.blit(start, (WIDTH//2-140, HEIGHT//2-60))
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()