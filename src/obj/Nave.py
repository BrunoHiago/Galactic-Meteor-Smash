import pygame.image


class Nave(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("./src/img/nave_notAnim.png")
        self.image = pygame.transform.scale(self.image, (100, 60))
        self.pos = [10, 225]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.sped = 0
        self.aceleration = 0.8

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.sped -= self.aceleration
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.sped += self.aceleration
        else:
            self.sped *= 0.4

        self.rect.y += self.sped

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > 500:
            self.rect.bottom = 500
