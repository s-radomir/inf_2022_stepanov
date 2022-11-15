import pygame
from pygame.draw import *
from math import *
pygame.init()
pygame.display.set_caption('1')
FPS = 30
screen = pygame.display.set_mode((400, 400))
def background(l_dim, h_dim, h_back1, h_back2, h_back3, col_1, col_2, col_3):
    '''

    l_dim, h_dim: разрешение фона
    h_back1: высота первой области
    h_back2: высота второй области
    h_back3: высота третьей области
    col_1: цвет первой области
    col_2: цвет второй области
    col_3: цвет третьей области
    pass
    '''
    screen = pygame.display.set_mode((l_dim, h_dim))
    rect(screen, (col_1), (0, 0, l_dim, h_back1))
    rect(screen, (col_2), (0, h_back1, l_dim, h_back2))
    rect(screen, (col_3), (0, h_back1 + h_back2, l_dim, h_back3))

def cloud(a, b, x, y):
    '''
    Рисует облака
    a: длина облака
    b: высота облака
    x, y: координаты левого верхнего угла
    pass
    '''
    ellipse(screen, (255,255,255), (x, y, a, b) )
    ellipse(screen, (255, 255, 255), (x+a/2, y, a, b))
    ellipse(screen, (255, 255, 255), (x + a, y, a, b))
    sdvig = 0
    for i in range(4):
        ellipse(screen, (255, 255, 255), (x-10 +sdvig, y+b/2, a, b))
        sdvig +=a/2
def wave(l_wave):
    '''
    l_wave: длина волны
    pass
    '''
    line(screen, (0, 0, 0), (0, 300), (400,300), 2)
    step = 0
    for i in range(100):
        k = 0
        if i % 2 == 0:
            ellipse(screen, (255, 235, 0), (step, 300-l_wave/4, l_wave, l_wave))
        else:
            ellipse(screen, (0, 0, 255), (step, 300-l_wave/4, l_wave, l_wave))
        step += l_wave
        k += 1
def sun(x, y, size):
        '''
        Рисует солнце
        x, y: к-ты центра
        size: радиус солнца
        '''
        circle(screen, (255, 252, 0), (x, y), size)
def body_ship(x_0, y_0, a_0, b_0, col_corp,col_window, x_shift, y_shift, sim):
        '''
        Рисует корпус корабля
        x_0, y_0: к-ты левого верхнего угла корпуса
        a_0, b_0: длина и ширина корпуса
        col_corp: цвет корпуса
        col_window: цвет окна
        x_shift, y_shift: смещение корабля отн-но x_0, y_0
        sim: уменьшение отн-но a_0, b_0
        pass
        '''
        x_0 += x_shift
        y_0 += y_shift
        a_0 = a_0/sim
        b_0 = b_0/sim
        rect(screen, (col_corp), (x_0, y_0, a_0, b_0))
        x_1 = x_0 + a_0
        y_1 = y_0
        x_2 = x_0 + a_0
        y_2 = y_0 + b_0
        x_3 = x_0 + a_0+ 30
        y_3 = y_0
        polygon(screen, (col_corp), [(x_1, y_1), (x_2, y_2), (x_3, y_3)])
        delta_x = -25/sim
        x_arc = x_0 + delta_x
        y_arc = y_0 - b_0
        R = 50/sim
        arc(screen, (col_corp), (x_arc, y_arc, R, R), pi, 1.5*pi, 500)
        x_circle = x_0 + 0.75 * a_0
        y_circle = y_0 + 0.5 * b_0
        circle(screen, (255, 255, 255), (x_circle, y_circle), 8 / sim)
        circle(screen, (col_window), (x_circle, y_circle), 10 / sim, 2)
def sail(x_0, y_0, l_paluba, h_paluba, col_paluba, col_sail, x_shift, y_shift, sim):
    '''
    x_0, y_0: к-ты левого верхнего угла корпуса
    l_paluba, h_paluba: длина и ширина палубы
    col_paluba: цвет палубы
    col_sail: цвет паруса
    x_shift, y_shift: смещение корабля отн-но x_0, y_0
    pass
    '''
    x_paluba = x_0 + 40/sim + x_shift
    y_paluba = y_0 - 80/sim + y_shift
    l_paluba = l_paluba/sim
    h_paluba = h_paluba/sim
    rect(screen, (col_paluba), (x_paluba, y_paluba, l_paluba, h_paluba))
    x_parus1_1 = x_paluba + l_paluba
    y_parus1_1 = y_paluba
    x_parus1_2 = x_parus1_1 + 20/sim
    y_parus1_2 = y_parus1_1 + h_paluba/2
    x_parus1_3 = x_parus1_2 + 40/sim
    y_parus1_3 = y_parus1_2
    polygon(screen, (col_sail), [(x_parus1_1, y_parus1_1), (x_parus1_2, y_parus1_2), (x_parus1_3, y_parus1_3)])
    x_parus2_1 = x_paluba + l_paluba
    y_parus2_1 = y_paluba + h_paluba
    x_parus2_2 = x_parus1_2
    y_parus2_2 = y_parus1_2
    x_parus2_3 = x_parus1_3
    y_parus2_3 = y_parus1_3
    polygon(screen, (col_sail), [(x_parus2_1, y_parus2_1), (x_parus2_2, y_parus2_2), (x_parus2_3, y_parus2_3)])
def ship(x_0, y_0, a_0, b_0, l_paluba, h_paluba, x_shift, y_shift, sim, col_corp, col_window, col_paluba, col_sail):
    '''
    x_0, y_0: к-ты левого верхнего угла корпуса
    a_0, b_0: длина и ширина корпуса
    l_paluba, h_paluba: длина и ширина палубы
    col_corp: цвет корпуса
    col_window: цвет окна
    col_paluba: цвет палубы
    col_sail: цвет паруса
    x_shift, y_shift: смещение корабля отн-но x_0, y_0
    sim: уменьшение отн-но a_0, b_0
    :return:
    '''
    sim = sim
    body_ship(x_0, y_0, a_0, b_0, col_corp,col_window, x_shift, y_shift, sim)
    sail(x_0, y_0, l_paluba, h_paluba, col_paluba, col_sail, x_shift, y_shift, sim)
def umbrella(x_bas, y_bas, l_bas, h_bas, x_um_shift, y_um_shift, sim_um, col_umb):
    #Основание
    x_bas += x_um_shift
    y_bas += y_um_shift
    l_bas = l_bas/sim_um
    h_bas = h_bas/sim_um
    rect(screen, (col_umb), (x_bas, y_bas, l_bas, h_bas))
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
    polygon(screen, (col_umb), [(x_z_1, y_z_1), (x_z_2, y_z_2), (x_z_3, y_z_3), (x_z_4, y_z_4)])
    #Спицы
    line(screen, (0, 0, 0), (x_z_1, y_z_1), (x_z_4, y_z_4), 2)
    line(screen, (0, 0, 0), (x_z_1, y_z_1), (x_z_4 + 15, y_z_4), 2)
    line(screen, (0, 0, 0), (x_z_1, y_z_1), (x_z_4 + 30, y_z_4), 2)
    line(screen, (0, 0, 0), (x_z_2, y_z_2), (x_z_3, y_z_3), 2)
    line(screen, (0, 0, 0), (x_z_2, y_z_2), (x_z_3 - 15, y_z_3), 2)
    line(screen, (0, 0, 0), (x_z_2, y_z_2), (x_z_3 - 30, y_z_3), 2)

#Data
BROWN = (255, 113, 0) #body
WHITE = (0, 0, 0) #window
BLACK = (255, 0, 0) #paluba
BEIGE = (255, 252, 140) #sail
GREEN = (0, 253, 0) #umbrella
AZURE = (0, 255, 247) #sky
BLUE = (0, 0, 255) #sea
YELLOW = (255, 235, 0) #sand
l_dim = 400
h_dim = 400
h_back1 = 200
h_back2 = 100
h_back3 = 100
x_sun = 350
y_sun = 50
size_sun = 40
l_cloud = 30
h_cloud = 30
x_cloud = 50
y_cloud = 20
l_wave = 20
x_0 = 250
y_0 = 230
a_0 = 120
b_0 = 26
l_paluba = 8
h_paluba = 80
x_bas = 80
y_bas = 260
l_bas = 8
h_bas = 120

background(l_dim, h_dim, h_back1, h_back2, h_back3, AZURE, BLUE, YELLOW)
sun(x_sun, y_sun, size_sun)
cloud(l_cloud, h_cloud, x_cloud, y_cloud)
cloud(l_cloud+20, l_cloud+20, x_cloud+80, y_cloud)
cloud(l_cloud+20, h_cloud, x_cloud-20, y_cloud+80)
wave(l_wave)
umbrella(x_bas, y_bas, l_bas, h_bas, -50, -20, 1, GREEN)
umbrella(x_bas, y_bas, l_bas, h_bas, 60, 30, 1.5, GREEN)
ship(x_0, y_0, a_0, b_0, l_paluba, h_paluba, 0, 0, 1, BROWN, WHITE, BLACK, BEIGE)
ship(x_0, y_0, a_0, b_0, l_paluba, h_paluba, -100, -20, 2, BROWN, WHITE, BLACK, BEIGE)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()