import pygame
from pygame.draw import *

pygame.init()
pygame.display.set_caption('1')

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 150)
rect(screen, (0,0,0), (150, 240, 100, 25))

circle(screen, (255,0,0), (150,120), 30)
circle(screen, (255,0,0), (250,120), 25)

circle(screen, (0,0,0), (150,120), 15)
circle(screen, (0,0,0), (250,120), 12.5)

polygon(screen, (0, 0, 0), [(230,110), (220,100), (260,60), (280,70)])
#aalines(screen, (0, 0, 0), False, [(120,70), (110,80), (160,100), (180,80)])
polygon(screen, (0, 0, 0), [(120,70), (110,80), (190,110), (200,90)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()