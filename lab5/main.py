import pygame as pg
from pygame.draw import *
from math import *

pg.init()
FPS = 15
screen = pg.display.set_mode((1200, 700))


def ellipse_angle(surface, color, rect, angle, width=0):
    '''
    :param color: цвет
    :param rect: прямоугольник вписанный в эллипс (лист)
    :param angle: угол эллипса
    :param width: толщина
    :return: лист повернутый под углом
    '''
    target_rect = pg.Rect(rect)
    shape_surf = pg.Surface(target_rect.size, pg.SRCALPHA)
    pg.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pg.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))

def rotate_rect(color, x, y, a, b, alf):
    '''

    :param color: цвет
    :param x, y: координаты левого верхнего угла прямоугольника
    :param a, b: длина и ширина прямоугольника
    :param alf: угол под которых находится прямоугольник
    :return: прямоугольник (часть ствола бамбука) под углом
    '''
    polygon(screen, color, [(x, y), (x + a * cos(alf), y + a * sin(alf)),
                            (x + a * cos(alf) - b * sin(alf), y + a * sin(alf) + b * cos(alf)),
                            (x - b * sin(alf), y + b * cos(alf)), (x, y)])

def bamboo(x, y, sizex, sizey):
    '''

    :param x, y: координаты нижней части ствола
    :param sizex, sizey: растяжение вдоль горизонтальной и вертикальной оси
    :return: бамбук
    '''
    rect(screen, GREEN, (x, y, 25 * sizex, 70 * sizey))
    rect(screen, GREEN, (x, y - 100 * sizey, 25 * sizex, 90 * sizey))
    rotate_rect(GREEN, x + 18 * sizex, y - 170 * sizey, 19 * sizex, 60 * sizey, pi / 9 * sizex / sizey)
    rotate_rect(GREEN, x + 45 * sizex, y - 255 * sizey, 12 * sizex, 80 * sizey, pi / 9 * sizex / sizey)

    arc(screen, GREEN, (x + 25 * sizex, y - 140 * sizey, 150 * sizex, 225 * sizey), pi / 3, 2 * pi / 3 + 0.5, 2)
    arc(screen, (0, 125, 0), (x - 145 * sizex, y - 110 * sizey, 170 * sizex, 250 * sizey), pi / 3 - 0.5,
        2 * pi / 3 - 0.1, 2)

    arc(screen, GREEN, (x + 38 * sizex, y - 230 * sizey, 350 * sizex, 125 * sizey), pi / 2 + 0.1, pi - 0.15, 2)
    arc(screen, GREEN, (x - 350 * sizex, y - 200 * sizey, 350 * sizex, 140 * sizey), 0.1, pi / 2 - 0.05, 2)

    ellipse_angle(screen, GREEN, (x - 90 * sizex, y - 110 * sizey, 12 * sizex, 50 * sizey), -20)
    ellipse_angle(screen, GREEN, (x - 70 * sizex, y - 110 * sizey, 10 * sizex, 50 * sizey), -20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x - 48 * sizex, y - 100 * sizey, 10 * sizex, 50 * sizey), -20 * sizex / sizey)

    ellipse_angle(screen, GREEN, (x + 100 * sizex, y - 140 * sizey, 10 * sizex, 50 * sizey), 20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x + 120 * sizex, y - 140 * sizey, 10 * sizex, 50 * sizey), 20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x + 80 * sizex, y - 130 * sizey, 10 * sizex, 50 * sizey), 20 * sizex / sizey)

    ellipse_angle(screen, GREEN, (x - 150 * sizex, y - 197 * sizey, 10 * sizex, 50 * sizey), -20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x - 130 * sizex, y - 197 * sizey, 10 * sizex, 50 * sizey), -20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x - 110 * sizex, y - 192 * sizey, 10 * sizex, 50 * sizey), -20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x - 90 * sizex, y - 188 * sizey, 10 * sizex, 50 * sizey), -20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x - 60 * sizex, y - 177 * sizey, 10 * sizex, 50 * sizey), -20 * sizex / sizey)

    ellipse_angle(screen, GREEN, (x + 180 * sizex, y - 227 * sizey, 10 * sizex, 50 * sizey), 20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x + 160 * sizex, y - 227 * sizey, 10 * sizex, 50 * sizey), 20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x + 140 * sizex, y - 222 * sizey, 10 * sizex, 50 * sizey), 20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x + 120 * sizex, y - 218 * sizey, 10 * sizex, 50 * sizey), 20 * sizex / sizey)
    ellipse_angle(screen, GREEN, (x + 90 * sizex, y - 207 * sizey, 10 * sizex, 50 * sizey), 20 * sizex / sizey)

def panda_bb(x, y, sizex, sizey):
    '''
    :param x, y: координаты верхней части
    :param sizex, sizey: растяжение вдоль горизонтальной и вертикальной оси
    :return: корпус панды
    '''
    ellipse_angle(screen, WHITE, (x - 200 * sizex, y - 280 * sizey, 100 * sizex, 165 * sizey), 90 * sizex / sizey)
    ellipse_angle(screen, BLACK, (x - 260 * sizex, y - 197 * sizey, 35 * sizex, 140 * sizey), -5 * sizex / sizey)
    polygon(screen, BLACK, [[x - 250 * sizex, y - 57 * sizey], [x - 230 * sizex, y - 45 * sizey],
                            [x - 200 * sizex, y - 80 * sizey], [x - 210 * sizex, y - 200 * sizey]])
    polygon(screen, BLACK, [[x - 140 * sizex, y - 223 * sizey], [x - 140 * sizex, y - 120 * sizey], [x - 150 * sizex, y - 60 * sizey],
                            [x - 180 * sizex, y - 25 * sizey], [x - 205 * sizex, y - 50 * sizey]])
    ellipse_angle(screen, BLACK, (x - 210 * sizex, y - 80 * sizey, 30 * sizex, 50 * sizey), -70 * sizex / sizey)
    ellipse_angle(screen, BLACK, (x - 210 * sizex, y - 65 * sizey, 30 * sizex, 50 * sizey), 70 * sizex / sizey)
    ellipse_angle(screen, BLACK, (x - 130 * sizex, y - 200 * sizey, 45 * sizex, 135 * sizey), -18 * sizex / sizey)
    ellipse_angle(screen, BLACK, (x - 145 * sizex, y - 105 * sizey, 30 * sizex, 45 * sizey), 72 * sizex / sizey)
    polygon(screen, BLACK,
            [[x - 190 * sizex, y - 90 * sizey], [x - 95 * sizex, y - 150 * sizey], [x - 110 * sizex, y - 100 * sizey]])

def panda_f(x, y, sizex, sizey):
    '''
    :param x, y: координаты верхней части
    :param sizex, sizey: растяжение вдоль горизонтальной и вертикальной оси
    :return: голова панды
    '''
    ellipse_angle(screen, WHITE, (x - 200 * sizex, y - 197 * sizey, 20 * sizex, 100 * sizey), -70 * sizex / sizey)
    ellipse_angle(screen, WHITE, (x - 182 * sizex, y - 270 * sizey, 35 * sizex, 115 * sizey), 20 * sizex / sizey)
    ellipse_angle(screen, WHITE, (x - 223 * sizex, y - 287 * sizey, 10 * sizex, 85 * sizey), -60 * sizex / sizey)
    ellipse_angle(screen, WHITE, (x - 250 * sizex, y - 227 * sizey, 10 * sizex, 100 * sizey), 12 * sizex / sizey)
    polygon(screen, WHITE,[[x -180 * sizex, y - 265 * sizey],[x - 155 * sizex, y - 160 * sizey],
                           [x - 235 * sizex, y - 130 * sizey], [x - 255 * sizex, y - 225 * sizey]])
    ellipse_angle(screen, BLACK, (x - 210 * sizex, y - 185 * sizey, 30 * sizex, 30 * sizey), -70 * sizex / sizey)
    ellipse_angle(screen, BLACK, (x - 255 * sizex, y - 195 * sizey, 25 * sizex, 33 * sizey), 0 * sizex / sizey)
    ellipse_angle(screen, BLACK, (x - 245 * sizex, y - 145 * sizey, 30 * sizex, 25 * sizey), 0 * sizex / sizey)
    ellipse_angle(screen, BLACK, (x - 255 * sizex, y - 260 * sizey, 25 * sizex, 50 * sizey), 130 * sizex / sizey)
    ellipse_angle(screen, BLACK, (x - 170 * sizex, y - 250 * sizey, 25 * sizex, 50 * sizey), 20 * sizex / sizey)

def panda(x,y,sizex,sizey):
    '''
    :param x, y: координаты верхней части
    :param sizex, sizey: растяжение вдоль горизонтальной и вертикальной оси
    :return: панда
    '''
    panda_bb(x,y,sizex,sizey)
    panda_f(x,y,sizex,sizey)


GREEN = (0, 125, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill((255, 180, 140))

bamboo(600, 400, 1.25, 1.45)
bamboo(1000, 400, 0.85, 1.40)
bamboo(250, 430, 0.45 * 1.25, 0.65 * 1.25)
bamboo(450, 450, 0.45 * 1.25, 0.75 * 1.25)
panda(1000, 700, 1.35, 1.35)
panda(650, 700, 0.60, 0.60)

pg.display.update()
clock = pg.time.Clock()
fina = False

while not fina:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fina = True

pg.quit()