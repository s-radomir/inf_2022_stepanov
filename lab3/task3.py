import pygame
from pygame.draw import *
from math import *

pygame.init()
pygame.display.set_caption('1')

FPS = 30
screen = pygame.display.set_mode((400, 400))

#Фон
rect(screen, (0, 255, 247), (0, 0, 400, 400))
rect(screen, (0, 0, 255), (0, 200, 400, 100))
rect(screen, (255, 235, 0), (0, 300, 400, 100))

#Волны
line(screen, (0, 0, 0), (0, 300), (400,300), 2)
step = 0
for i in range(8):
    if i % 2 == 0:
        ellipse(screen, (255, 235, 0), (step, 300-25/2, 50, 25))
    else:
        ellipse(screen, (0, 0, 255), (step, 300-25/2, 50, 25))
    step += 50


#arc(screen, (255, 235, 0), (100, 300, 5500, 6000), 0, pi)
#Облака
l_cloud = 30
h_cloud = 30
x_cloud = 50
y_cloud = 20
def cloud(a,b,x,y ,type=int):
    ellipse(screen, (255,255,255), (x, y, a, b) )
    ellipse(screen, (255, 255, 255), (x+a/2, y, a, b))
    ellipse(screen, (255, 255, 255), (x + a, y, a, b))
    sdvig = 0
    for i in range(4):
        ellipse(screen, (255, 255, 255), (x-10 +sdvig, y+b/2, a, b))
        sdvig +=a/2

#Солнце circle(screen, (255, 252, 0), (350, 50), 40)

#Корабль
def ship(x_shift, y_shift, sim):
    #Трюм
    x_0 = 250+x_shift
    y_0 = 230+y_shift
    a_0 = 120/sim
    b_0 = 26/sim
    rect(screen, (255, 113, 0), (x_0, y_0, a_0, b_0))
    #Нос
    x_1 = x_0 + a_0
    y_1 = y_0
    x_2 = x_0 + a_0
    y_2 = y_0 + b_0
    x_3 = x_0 + a_0+ 30
    y_3 = y_0
    polygon(screen, (255, 113, 0), [(x_1, y_1), (x_2, y_2), (x_3, y_3)])
    #Корма
    delta_x = -25/sim
    x_arc = x_0 + delta_x
    y_arc = y_0 - b_0
    R = 50/sim
    arc(screen, (255, 113, 0), (x_arc, y_arc, R, R), pi, 1.5*pi, 500)
    #Палуба
    x_paluba = x_0 + 40/sim
    y_paluba = y_0 - 80/sim
    l_paluba = 8/sim
    h_paluba = 80/sim
    rect(screen, (255, 0, 0), (x_paluba, y_paluba, l_paluba, h_paluba))
    #Парус
    x_parus1_1 = x_paluba + l_paluba
    y_parus1_1 = y_paluba
    x_parus1_2 = x_parus1_1 + 20/sim
    y_parus1_2 = y_parus1_1 + h_paluba/2
    x_parus1_3 = x_parus1_2 + 40/sim
    y_parus1_3 = y_parus1_2
    polygon(screen, (255, 252, 140), [(x_parus1_1, y_parus1_1), (x_parus1_2, y_parus1_2), (x_parus1_3, y_parus1_3)])
    x_parus2_1 = x_paluba + l_paluba
    y_parus2_1 = y_paluba + h_paluba
    x_parus2_2 = x_parus1_2
    y_parus2_2 = y_parus1_2
    x_parus2_3 = x_parus1_3
    y_parus2_3 = y_parus1_3
    polygon(screen, (255, 252, 140), [(x_parus2_1, y_parus2_1), (x_parus2_2, y_parus2_2), (x_parus2_3, y_parus2_3)])
    #Окно
    x_circle = x_0 + 0.75*a_0
    y_circle = y_0 + 0.5*b_0
    circle(screen, (255, 255, 255), (x_circle, y_circle), 8/sim)
    circle(screen, (0, 0, 0), (x_circle, y_circle), 10/sim, 2)


#Зонт
def umbrella(x_um_shift, y_um_shift, sim_um):
    #Основание
    x_bas = 80 + x_um_shift
    y_bas = 260 + y_um_shift
    l_bas = 8/sim_um
    h_bas = 120/sim_um
    rect(screen, (0, 253, 0), (x_bas, y_bas, l_bas, h_bas))
    #Зонт
    x_z_1 = x_bas
    y_z_1 = y_bas
    x_z_2 = x_bas + l_bas
    y_z_2 = y_bas
    delta_x_umb = 50/sim_um
    delta_y_bas = 30/sim_um
    x_z_3 = x_z_2 + delta_x_umb
    y_z_3 = y_z_2 + delta_y_bas
    x_z_4 = x_z_1 - delta_x_umb
    y_z_4 = y_z_1 + delta_y_bas
    polygon(screen, (0, 253, 0), [(x_z_1, y_z_1), (x_z_2, y_z_2), (x_z_3, y_z_3), (x_z_4, y_z_4)])
    #Спицы
    line(screen, (0, 0, 0), (x_z_1, y_z_1), (x_z_4, y_z_4), 2)
    line(screen, (0, 0, 0), (x_z_1, y_z_1), (x_z_4 + 15, y_z_4), 2)
    line(screen, (0, 0, 0), (x_z_1, y_z_1), (x_z_4 + 30, y_z_4), 2)
    line(screen, (0, 0, 0), (x_z_2, y_z_2), (x_z_3, y_z_3), 2)
    line(screen, (0, 0, 0), (x_z_2, y_z_2), (x_z_3 - 15, y_z_3), 2)
    line(screen, (0, 0, 0), (x_z_2, y_z_2), (x_z_3 - 30, y_z_3), 2)


cloud(l_cloud, h_cloud, x_cloud, y_cloud)
cloud(l_cloud+20, l_cloud+20, x_cloud+80, y_cloud)
cloud(l_cloud+20, h_cloud, x_cloud-20, y_cloud+80)
circle(screen, (255, 252, 0), (350, 50), 40)
ship(0, 0, 1)
ship(-200, -20, 2)
umbrella(-50, -20, 1)
umbrella(60, 30, 1.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()