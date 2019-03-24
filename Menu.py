import Game
import pygame


def Menu():
    # define some keys:
    keyStrartPlay = ' '
    # define colors:
    clBackGround = (200, 200, 80)
    pygame.init()
    size = (840, 600)
    window = pygame.display.set_mode(size)
    pygame.display.set_caption('Labirint')
    pygame.font.init()
    comicSansFont = pygame.font.SysFont('Purisa', 40)
    text1 = comicSansFont.render('Press SPACE to start', True, (70, 0, 0))
    text1Pos = text1.get_rect()
    text1Pos.midtop = (420, 250)
    text2 = comicSansFont.render('Press ESC to exit', True, (70, 0, 0))
    text2Pos = text2.get_rect()
    text2Pos.midtop = (420, 350)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if chr(event.key) == keyStrartPlay:
                    run = not Game.Game(window)
                elif event.key == 27:
                    run = False
        pygame.draw.rect(window, clBackGround, (0, 0, 840, 600))
        # window.blit(text, (100, 260))
        window.blit(text1, text1Pos)
        window.blit(text2, text2Pos)
        pygame.display.update()
    pygame.quit()


pygame.init()
Menu()
