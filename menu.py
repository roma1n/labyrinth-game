from game import Game
import pygame
from player_controller import key_escape, key_start_play


def menu():
    # define colors:
    cl_back_ground = (200, 200, 80)
    size = (840, 600)
    window = pygame.display.set_mode(size)
    pygame.display.set_caption('Labyrinth')
    pygame.font.init()
    font = pygame.font.SysFont('Purisa', 40)
    text1 = font.render('Press SPACE to start', True, (70, 0, 0))
    text1_pos = text1.get_rect()
    text1_pos.midtop = (420, 250)
    text2 = font.render('Press ESC to exit', True, (70, 0, 0))
    text2_pos = text2.get_rect()
    text2_pos.midtop = (420, 350)
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == key_start_play:
                    game = Game()
                    run = not game.play(window)
                elif event.key == key_escape:
                    run = False
        pygame.draw.rect(window, cl_back_ground, (0, 0, 840, 600))
        window.blit(text1, text1_pos)
        window.blit(text2, text2_pos)
        pygame.display.update()
    pygame.quit()


pygame.init()
menu()
