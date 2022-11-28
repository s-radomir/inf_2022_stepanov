import math
from random import choice
from random import randint
import pygame
import time

pygame.init()

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Ball:
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = tank.x
        self.y = tank.y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.vy += 1
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= WIDTH:
            self.vx = -self.vx // 2
            if self.vx < 1:
                self.x = WIDTH - self.r
        if self.y + self.r >= HEIGHT - 50:
            self.vy = -self.vy // 2
            self.vx = self.vx // 2
            if abs(self.vy) < 0.1:
                self.y = HEIGHT - 50 - self.r
                self.vx = 0
                self.vy = 0

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
        obj: Обьект, с которым проверяется столкновение.
        Returns:
        Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if ((self.x - obj.x)**2 + (self.y - obj.y)**2) <= (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Tank:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.an1 = 1
        self.color = GREY
        self.x = 40
        self.y = 460
        self.vx = 5

    def move_right(self, event):
        if self.x > WIDTH - 40:
            self.x += 0
        else:
            self.x += self.vx


    def move_left(self, event):
        if self.x < 40:
            self.x += 0
        else:
            self.x += -self.vx


    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        try:
            self.an1 = math.atan2((event.pos[1]-self.y), (event.pos[0] - self.x))
        except:
            self.an1 = 0
        if event:
            try:
                self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
            except:
                self.an = 0
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # FIXIT don't know how to do it
        pygame.draw.polygon(
            self.screen,
            GREEN,
            [(self.x - 45, self.y),
             (self.x + 45, self.y),
             (self.x + 45, self.y + 20),
             (self.x - 45, self.y + 20)
             ])

        pygame.draw.circle(
            self.screen,
            GREEN,
            (self.x + 30, self.y+35),
            15
        )

        pygame.draw.circle(
            self.screen,
            GREEN,
            (self.x, self.y + 35),
            15
        )

        pygame.draw.circle(
            self.screen,
            GREEN,
            (self.x - 30, self.y + 35),
            15
        )

        pygame.draw.polygon(screen, self.color,
                            [[self.x, self.y],
                             [self.x + 2 * self.f2_power * math.cos(self.an1), self.y + 2 * self.f2_power * math.sin(self.an1)],
                             [self.x + 2* self.f2_power * math.cos(self.an1) + 3 * math.sin(self.an1),
                              self.y + 2 * self.f2_power * math.sin(self.an1) - 3 * math.cos(self.an1)],
                             [self.x + 3 * math.sin(self.an1), self.y - 3 * math.cos(self.an1)]])

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        """ Конструктор класса Target
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.live = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(600, 700)
        y = self.y = randint(100, 300)
        r = self.r = randint(2, 50)
        color = self.color = RED


    def draw(self):
        # create a surface object, image is drawn on it.
        pygame.draw.circle(screen,
            self.color,
            (self.x, self.y),
            self.r
        )



font_name = pygame.font.match_font('arial')



def draw_text(surf, text, size, x, y):
    '''
        Функция отображения счета
        surf - экран
        text - счет
        size - не очень большой размер
        x, y - координаты центра текста
    '''
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


bullet = 0
balls = []

targets =[]
points = 0

clock = pygame.time.Clock()
tank = Tank(screen)
t1 = Target()
t2 = Target()

targets.append(t1)
targets.append(t2)
finished = False
a = 0
hit_on = 0
while not finished:
    screen.fill(WHITE)
    tank.draw()
    for t in targets:
        t.draw()
    draw_text(screen, str(points), 26, 15, 10)
    if a == 1:
        draw_text(screen, 'Вы уничтожили цель за ' + str(bullet) + ' выстрелов', 26, WIDTH / 2, HEIGHT / 2 - 25)
        pygame.display.update()
        time.sleep(1)
        bullet = 0
        a = 0
    for b in balls:
        b.draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tank.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            tank.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            tank.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                tank.move_right(event)
            if event.key == pygame.K_LEFT:
                tank.move_left(event)



    for b in balls:
        if b.vy == 0:
            balls.remove(b)
        for t in targets:
            if b.hittest(t) and t.live:
                a = 1
                points += 1
                targets.remove(t)
                t_new = Target()
                targets.append(t_new)
                t.live = 1
                balls.remove(b)
        b.move()
    tank.power_up()


pygame.quit()