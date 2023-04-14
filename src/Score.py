import pygame.font


class Score:
    def __init__(self):
        self.score = 0
        self.position = (0, 0)

    def update(self):
        self.score += 1

    def draw(self, display):
        text = "Pontuaçao: " + str(self.score)
        font = pygame.font.Font(None, 32)
        textscore = font.render(text, True, (0, 255, 0))
        display.blit(textscore, self.position)
