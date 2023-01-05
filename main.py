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
clock = pygame.time.Clock()
pygame.display.set_caption('Собери яблоки!')


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
        super().__init__(sprites)
        self.image = Apple.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if True:
            self.rect = self.rect.move(0, 1)


class BadApple(pygame.sprite.Sprite):
    image = load_image('bad apple.png')

    def __init__(self, pos):
        super().__init__(sprites)
        self.image= BadApple.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if True:
            self.rect = self.rect.move(0, 1)

running = True
background = Background()
start1 = time.time()
start2 = time.time()
apple_interval = 2  # интервал, с которым появляются обычные яблоки
bad_apple_interval = 5  # интервал, с которым появляются плохие яблоки
while running:
    sprites.update()
    now1 = time.time()
    now2 = time.time()
    if now1 - start1 > apple_interval:
        Apple([random.randint(20, 760), random.randint(0, 20)])
        start1 = now1
    if now2 - start2 > bad_apple_interval:
        BadApple([random.randint(20, 760), random.randint(0, 20)])
        start2 = now2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pass
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(40)

pygame.quit()
