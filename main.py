import pygame
import asyncio
import random
from src.obj.Nave import Nave
from src.obj.Meteoro import Meteoro
from src.obj.Bala import Bala
from src.Score import Score
from src import HomeScreen
from src.obj.Particle import Particle

def desenhar_vidas(display, lives, width):
    font = pygame.font.Font(None, 32)
    text = f"Vidas: {lives}"
    text_surface = font.render(text, True, (255, 50, 50))
    display.blit(text_surface, (width - text_surface.get_width() - 10, 10))

async def main():
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
    lives = 3
    particles = []

    # sons
    explosion = pygame.mixer.Sound("./src/sounds/explosao.ogg")

    # placar
    score = Score()
    score.draw(display)

    # Home Screen
    homeScreen = True

    while loop:

        if homeScreen:
            homeScreen = await HomeScreen.tela_inicio(width, height, background, display)
            # Inicializar/reiniciar estado do jogo após sair da tela inicial
            lives = 3
            score.score = 0
            level = 1
            cont = 1.0
            meteorGroup.empty()
            objectGroup.empty()
            balaGroup.empty()
            nave = Nave(objectGroup)
            particles.clear()

        if score.score > level * 10:
            level += 1
        if cont >= max(2.5, 10 - level):
            meteorGroup.add(Meteoro(level, objectGroup, meteorGroup))
            cont = 0.1

        cont *= 1.1

        # Rastro de partículas da nave
        if not homeScreen:
            for _ in range(2):
                particles.append(Particle(
                    nave.rect.left + 5,
                    nave.rect.centery + random.randint(-5, 5),
                    random.choice([(255, 100, 0), (255, 180, 0), (255, 50, 0)]),
                    random.uniform(3, 5),
                    random.uniform(-4, -1),
                    random.uniform(-1, 1),
                    random.randint(8, 15)
                ))

        # Colisoes
        collision = pygame.sprite.spritecollide(
            nave, meteorGroup, True, pygame.sprite.collide_mask)

        if collision:
            lives -= 1
            explosion.play()
            # Partículas de explosão da nave
            for _ in range(25):
                particles.append(Particle(
                    nave.rect.centerx,
                    nave.rect.centery,
                    random.choice([(255, 50, 0), (255, 150, 0), (255, 255, 0), (100, 100, 100)]),
                    random.uniform(4, 8),
                    random.uniform(-6, 6),
                    random.uniform(-6, 6),
                    random.randint(15, 30)
                ))
            if lives <= 0:
                homeScreen = True

        collisionBala = pygame.sprite.groupcollide(
            balaGroup, meteorGroup, True, True, pygame.sprite.collide_mask)
        if collisionBala:
            score.update()
            explosion.play()
            # Partículas de explosão do meteoro
            for bullets, meteors in collisionBala.items():
                for met in meteors:
                    for _ in range(15):
                        particles.append(Particle(
                            met.rect.centerx,
                            met.rect.centery,
                            random.choice([(150, 150, 150), (100, 100, 100), (255, 100, 0), (255, 50, 0)]),
                            random.uniform(3, 6),
                            random.uniform(-4, 4),
                            random.uniform(-4, 4),
                            random.randint(10, 25)
                        ))

        # fechar a tela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Bala(nave, objectGroup, balaGroup)

        # Meteoros que ultrapassam a tela reduzem vida
        for met in meteorGroup:
            if met.rect.x < 0:
                met.kill()
                lives -= 1
                if lives <= 0:
                    homeScreen = True

        display.blit(background, (0, 0))

        # Atualizar e desenhar partículas
        for p in particles[:]:
            p.update()
            if p.lifetime <= 0 or p.size <= 0:
                particles.remove(p)
            else:
                p.draw(display)

        objectGroup.update()

        objectGroup.draw(display)
        score.draw(display)
        desenhar_vidas(display, lives, width)

        pygame.display.update()
        pygame.time.delay(30)
        pygame.display.flip()

        await asyncio.sleep(0)

asyncio.run(main())
