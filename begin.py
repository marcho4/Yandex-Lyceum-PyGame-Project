#  оч сыро точно накидаем всяких фишек
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


size = 600, 600
screen = pygame.display.set_mode(size)
screen.fill('white')
pygame.display.set_caption('Start game')
sprites = pygame.sprite.Group()
poster = Poster(sprites, size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            running = False
            #  перекидываем на экран уровня
    sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
