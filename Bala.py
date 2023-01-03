import pygame.sprite


class Bala(pygame.sprite.Sprite):
    def __init__(self, nave, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("./img/bala.png")
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()
        self.speed = 10
        self.rect.center = nave.rect.midright

    def update(self):
        self.rect.x += self.speed

