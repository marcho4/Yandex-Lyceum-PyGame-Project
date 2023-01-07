import random
import time

import pygame


def load_image(name):
    image = pygame.image.load(f"{'data'}/{name}")
    return image


class Poster(pygame.sprite.Sprite):
    def __init__(self, group, size):
        super().__init__(group)
        self.width, self.height = size
        Poster.image = load_image('game_start.png')
        self.image = Poster.image
        self.rect = self.image.get_rect()
        self.rect.x = 140
        self.rect.y = 219
        pygame.font.init()
        f1 = pygame.font.Font(None, 60)
        r1 = f1.render(f'Press SPACE to play!', True, 'black')
        screen.blit(r1, (90, 400))


size = 600, 600
screen = pygame.display.set_mode(size)
screen.fill('white')
pygame.display.set_caption('Start game')
post = pygame.sprite.Group()
poster = Poster(post, size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
                run = True
    post.draw(screen)
    pygame.display.flip()


sprites = pygame.sprite.Group()
apples = pygame.sprite.Group()
lives = pygame.sprite.Group()
clock = pygame.time.Clock()
pygame.display.set_caption('Собери яблоки!')
missed_apples = 0
collected_apples = 0
bad_apples_collected = 0
pygame.font.init()
font = pygame.font.Font(None, 44)
s = 0


# Задний фон
class Background(pygame.sprite.Sprite):
    image = load_image('apple garden.png')
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    def __init__(self):
        super().__init__(sprites)
        self.width, self.height = size
        self.image = Background.image
        self.rect = self.image.get_rect()

    def update(self):
        if s == 0:
            render = font.render(f'Press <-- or --> to start the game', True, 'red')
            screen.blit(render, (85, 170))
        elif bad_apples_collected == 3:
            render = font.render(f'You missed with the score {collected_apples}!', True, 'red')
            screen.blit(render, (200, 300))
        else:
            render = font.render(f'Your score: {collected_apples}', True, 'red')
            screen.blit(render, (10, 50))
        pygame.display.flip()


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
                lives.update()
                self.kill()


class Lives(pygame.sprite.Sprite):
    image = load_image('life.png')

    def __init__(self, pos):
        super().__init__(lives)
        self.image = Lives.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if bad_apples_collected == 1:
            l3.kill()
        elif bad_apples_collected == 2:
            l2.kill()
        else:
            l1.kill()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, desired_row, x, y):
        super().__init__(sprites)
        self.elapsed = 0
        self.frames = []
        self.t = False
        self.d = desired_row
        if self.d == 2:
            desired_row = 3
        elif self.d == 1:
            desired_row = 4
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
        for j in range(columns):
            for i in range(rows):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
        if self.t:
            self.frames = self.frames[self.desired_row:]
        else:
            self.frames = self.frames[self.desired_row:self.last_i]

    def move(self, movement):
        x, y = self.rect.x, self.rect.y
        if movement == "left":
            if x > min_x:
                self.rect.x -= 10
        elif movement == "right":
            if x < max_x - 1:
                self.rect.x += 10

    def update(self):
        self.cur_frame = (self.cur_frame - 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


background = Background()
bro = AnimatedSprite(load_image('bro.png'), 4, 4, 1, 400, 490)
l1 = Lives((600, 40))
l2 = Lives((650, 40))
l3 = Lives((700, 40))
start1 = time.time()
start2 = time.time()
apple_interval = 2  # интервал, с которым появляются обычные яблоки
bad_apple_interval = 5  # интервал, с которым появляются плохие яблоки
max_x = 720
min_x = 0
run = True
while run:
    keys = pygame.key.get_pressed()
    now1 = time.time()
    now2 = time.time()
    if keys[pygame.K_RIGHT]:
        s = 1
        bro.move("right")
        sprites.update()
    if keys[pygame.K_LEFT]:
        s = 1
        bro.move("left")
        sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if bad_apples_collected == 3:
            run = False
        if now1 - start1 > apple_interval:
            Apple([random.randint(20, 760), random.randint(0, 20)])
            start1 = now1
        if now2 - start2 > bad_apple_interval:
            BadApple([random.randint(20, 760), random.randint(0, 20)])
            start2 = now2
    sprites.draw(screen)
    apples.draw(screen)
    lives.draw(screen)
    apples.update()
    background.update()
    pygame.display.flip()
    clock.tick(100)

pygame.quit()
