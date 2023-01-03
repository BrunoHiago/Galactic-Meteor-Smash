import pygame
from Nave import Nave
from Meteoro import Meteoro
from Bala import Bala

if __name__ == '__main__':
    pygame.init()
    width = 700
    heigth = 500
    display = pygame.display.set_mode([width, heigth])
    pygame.display.set_caption("Asteroid")

    # Grupo de Objeto
    meteorogroup = pygame.sprite.Group()
    objectGroup = pygame.sprite.Group()
    balaGroup = pygame.sprite.Group()


    nave = Nave(objectGroup)
    cont = 1.0
    nivel = 1
    loop = True
    pontuacao = 0

    # sons
    explosion = pygame.mixer.Sound("./sounds/explosao.wav")

    # fonte e texto
    font = pygame.font.Font(None, 32)
    text = "Pontuaçao: " + str(pontuacao)
    text_pontuacao = font.render(text, True, (0, 255, 0))
    text_react = text_pontuacao.get_rect()
    text_react.topright = (0, 0)

    while loop:

        if pontuacao > nivel * 10:
            nivel += 1
        if cont >= 2:
            meteorogroup.add(Meteoro(nivel, objectGroup, meteorogroup))
            cont = 0.1

        cont *= 1.1

        colision = pygame.sprite.spritecollide(nave, meteorogroup, True, pygame.sprite.collide_mask)
        if colision:
            loop = False

        colisionBala = pygame.sprite.groupcollide(balaGroup, meteorogroup, True, True, pygame.sprite.collide_mask)
        if colisionBala:
            pontuacao += 1
            explosion.play()

        # fechar a tela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Bala(nave, objectGroup, balaGroup)
        display.fill((0, 0, 0))

        objectGroup.update()
        objectGroup.draw(display)
        text = "Pontuaçao: " + str(pontuacao)
        text_pontuacao = font.render(text, True, (0, 255, 0))
        display.blit(text_pontuacao, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)
        pygame.display.flip()
