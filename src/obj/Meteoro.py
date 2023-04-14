import random

import pygame.image


class Meteoro(pygame.sprite.Sprite):
    def __init__(self, level, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("./src/img/meteoro.png")
        self.pos = [700, random.randrange(0, 500 - self.image.get_height())]
        self.spd = 1 + level + random.random()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        self.rect.x -= self.spd
