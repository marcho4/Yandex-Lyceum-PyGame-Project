import random
import time

import pygame


def load_image(name):
    image = pygame.image.load(f"{'data'}/{name}")
    return image


pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
sprites = pygame.sprite.Group()
apples = pygame.sprite.Group()
clock = pygame.time.Clock()
pygame.display.set_caption('Собери яблоки!')
missed_apples = 0
collected_apples = 0
bad_apples_collected = 0


# Задний фон
class Background(pygame.sprite.Sprite):
    image = load_image('apple garden.png')

    def __init__(self):
        super().__init__(sprites)
        self.width, self.height = size
        self.image = Background.image
        self.rect = self.image.get_rect()


# Обычное яблоко
class Apple(pygame.sprite.Sprite):
    image = load_image("apple.png")

    def __init__(self, pos):
        super().__init__(apples)
        self.image = Apple.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        global missed_apples, collected_apples
        if True:
            self.rect = self.rect.move(0, 1)
            if self.rect.y > 600:
                self.kill()
                missed_apples += 1
            if pygame.sprite.collide_mask(self, bro):
                collected_apples += 1
                self.kill()


# Плохое яблоко
class BadApple(pygame.sprite.Sprite):
    image = load_image('bad apple.png')

    def __init__(self, pos):
        super().__init__(apples)
        self.image = BadApple.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        global bad_apples_collected
        if True:
            self.rect = self.rect.move(0, 1)
            if self.rect.y > 600:
                self.kill()
            if pygame.sprite.collide_mask(self, bro):
                bad_apples_collected += 1
                self.kill()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, desired_row, x, y):
        super().__init__(sprites)
        self.elapsed = 0
        self.frames = []
        self.t = False
        self.desired_row = columns * (rows - desired_row + 1) * (-1)
        if rows - desired_row != 0:
            self.last_i = (rows - desired_row) * columns * -1
        elif rows - desired_row == 0:
            self.last_i = -1
            self.t = True
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
        if self.t:
            self.frames = self.frames[self.desired_row:]
        else:
            self.frames = self.frames[self.desired_row:self.last_i]

    def update(self):
        self.cur_frame = (self.cur_frame - 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


background = Background()
bro = AnimatedSprite(load_image('bro.png'), 4, 4, 4, 400, 490)
start1 = time.time()
start2 = time.time()
apple_interval = 2  # интервал, с которым появляются обычные яблоки
bad_apple_interval = 5  # интервал, с которым появляются плохие яблоки
max_x = 720
min_x = 0


def move(hero, movement):
    x, y = hero.rect.x, hero.rect.y
    if movement == "left":
        if x > min_x:
            hero.rect.x -= 10
    elif movement == "right":
        if x < max_x - 1:
            hero.rect.x += 10


running = True
while running:
    apples.update()
    keys = pygame.key.get_pressed()
    now1 = time.time()
    now2 = time.time()
    if keys[pygame.K_RIGHT]:
        move(bro, "right")
    if keys[pygame.K_LEFT]:
        move(bro, "left")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if bad_apples_collected == 3 or missed_apples == 10:
            running = False  # завершение игры если 3 гнилых яблока собрали или если 10 яблок пропустили
            print('you missed')
        if now1 - start1 > apple_interval:
            Apple([random.randint(20, 760), random.randint(0, 20)])
            start1 = now1
        if now2 - start2 > bad_apple_interval:
            BadApple([random.randint(20, 760), random.randint(0, 20)])
            start2 = now2
        sprites.update()
    sprites.draw(screen)
    apples.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
