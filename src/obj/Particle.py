import pygame

class Particle:
    def __init__(self, x, y, color, size, speed_x, speed_y, lifetime):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.lifetime = lifetime
        self.max_lifetime = lifetime

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.lifetime -= 1
        if self.size > 0.1:
            self.size -= 0.15

    def draw(self, surface):
        if self.lifetime > 0 and self.size > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))
