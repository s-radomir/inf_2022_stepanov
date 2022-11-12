import pygame
from pygame.draw import *
from math import *

pygame.init()
pygame.display.set_caption('1')

FPS = 30
screen = pygame.display.set_mode((400, 400))

#Фон
rect(screen, (0,255,247), (0,0,400,400))
rect(screen, (0,0,247), (0,200,400,100))
rect(screen, (255,235,0), (0,300,400,100))

x = 30
y = 30
def cloud(x,y, type=int):
    ellipse(screen, (255,255,255), (50, 20,x,y) )
    ellipse(screen, (255, 255, 255), (50+x/2, 20, x, y))
    ellipse(screen, (255, 255, 255), (50 + x, 20, x, y))
    sdvig = 0
    for i in range(4):
        ellipse(screen, (255, 255, 255), (40 +sdvig, 20+y/2, x, y))
        sdvig +=x/2

cloud(x,y)

#Солнце
circle(screen, (255,252,0), (350,50), 40)

#Корабль
rect(screen, (255,113,0), (250, 230, 120,26))
polygon(screen,(255,113,0), [(370,230), (370,256), (400,230)])
#arc(Surface, color, Rect, start_angle, stop_angle, wiph=1)
arc(screen, (255,113,0), (225,206,50,50), pi, 1.5*pi, 500)
rect(screen, (0,0,0), (290,150, 8, 80))
polygon(screen, (255,252,140), [(298,150), (338,190), (308,190)])
polygon(screen, (255,252,140), [(298,230), (338,190), (308,190)])
circle(screen, (255,255,255), (350,240), 8)
circle(screen, (0,0,0), (350,240), 10,2)

#Зонт
rect(screen, (0,253,0), (80,260,8,120))
polygon(screen, (0,253,0), [(80,260), (88,260), (138, 290), (30,290)])
line(screen, (0,0,0), (80,260),(45,290),2)
line(screen, (0,0,0), (80,260),(60,290),2)
line(screen, (0,0,0), (80,260),(30,290),2)

line(screen, (0,0,0), (88,260),(138,290),2)
line(screen, (0,0,0), (88,260),(123,290),2)
line(screen, (0,0,0), (88,260),(108,290),2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()