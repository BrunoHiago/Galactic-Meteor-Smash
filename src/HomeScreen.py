import pygame

def tela_inicio(width, height, background, display):
    pygame.init()

    fonte_titulo = pygame.font.Font(None, 64)
    titulo = fonte_titulo.render("Galactic Meteor Smash", True, (255, 255, 255))
    display.blit(background, (0, 0))
    display.blit(titulo, (width/2 - titulo.get_width()/2, height*0.15))

    # Renderizar botão de iniciar
    fonte_botao = pygame.font.Font(None, 32)
    playButton = fonte_botao.render("Iniciar", True, (255, 255, 255))
    playButton_rect = playButton.get_rect() # Criar um objeto pygame.Rect para a superfície do botão
    playButton_rect.center = (width/2, height * 0.70) # Definir a posição do botão na tela
    display.blit(playButton, playButton_rect) # Usar o objeto pygame.Rect para posicionar o botão na tela

    # Renderizar botão de Sair

    quitButton = fonte_botao.render("Sair", True, (255, 255, 255))
    quitButton_react = quitButton.get_rect()
    quitButton_react.center = (width/2, height * 0.80)
    display.blit(quitButton, quitButton_react)

    pygame.display.flip()

    playGame = False

    while not playGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Verificar clique no botão de iniciar
            
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1: # 1 é o botão esquerdo do mouse
                if playButton_rect.collidepoint(event.pos): # Verificar se o clique foi no botão de iniciar
                    playGame = True
                elif quitButton_react.collidepoint(event.pos):
                    pygame.quit()
                    quit()
    
    return False