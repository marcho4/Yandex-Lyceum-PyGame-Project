import pygame


def load_image(name):
    image = pygame.image.load(f"{'data'}/{name}")
    return image


class Poster(pygame.sprite.Sprite):
    def __init__(self, group, size):
        super().__init__(group)
        self.width, self.height = size
        Poster.image = load_image('gameover.png')
        self.image = Poster.image
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self):
        if self.rect.x == self.width - self.rect.width:
            pass
        else:
            self.rect.x += 1
            self.image = Poster.image


size = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game over')
sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
poster = Poster(sprites, size)
c = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and c > 650:
            running = False
    screen.fill('green')
    sprites.draw(screen)
    sprites.update()
    pygame.display.flip()
    clock.tick(200)
    c += 1

pygame.quit()
