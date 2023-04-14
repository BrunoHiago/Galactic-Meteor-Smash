import pygame
from src.obj.Nave import Nave
from src.obj.Meteoro import Meteoro
from src.obj.Bala import Bala
from src.Score import Score
from src import HomeScreen

if __name__ == '__main__':
    pygame.init()
    width = 700
    height = 500
    display = pygame.display.set_mode([width, height])
    pygame.display.set_caption("Galactic Meteor Smash")

    # Background
    background = pygame.image.load('./src/img/background.jpg')
    background = pygame.transform.scale(background, (width, height))

    # Grupo de Objeto
    meteorGroup = pygame.sprite.Group()
    objectGroup = pygame.sprite.Group()
    balaGroup = pygame.sprite.Group()

    nave = Nave(objectGroup)
    cont = 1.0
    level = 1
    loop = True

    # sons
    explosion = pygame.mixer.Sound("./src/sounds/explosao.wav")

    # placar
    score = Score()
    score.draw(display)

    # Home Screen
    homeScreen = True

    while loop:

        if homeScreen:
            homeScreen = HomeScreen.tela_inicio(width, height, background, display)
        if score.score > level * 10:
            level += 1
        if cont >= 10 - level:
            meteorGroup.add(Meteoro(level, objectGroup, meteorGroup))
            cont = 0.1

        cont *= 1.1

        # Colisoes
        collision = pygame.sprite.spritecollide(
            nave, meteorGroup, True, pygame.sprite.collide_mask)

        if collision:
            homeScreen = not homeScreen

        collisionBala = pygame.sprite.groupcollide(
            balaGroup, meteorGroup, True, True, pygame.sprite.collide_mask)
        if collisionBala:
            score.update()
            explosion.play()
        # /fim colisoes

        # fechar a tela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Bala(nave, objectGroup, balaGroup)

        for met in meteorGroup:
            if met.rect.x < 0:
                homeScreen = not homeScreen
        # /fim fechar a tela

        display.blit(background, (0, 0))

        objectGroup.update()

        objectGroup.draw(display)
        score.draw(display)

        pygame.display.update()
        pygame.time.delay(30)
        pygame.display.flip()
