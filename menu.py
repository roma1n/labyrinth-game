from game import Game
import pygame
from player_controller import key_escape, key_start_play


class Menu:
    def __init__(self):
        # define colors:
        self.cl_back_ground = (200, 200, 80)
        self.cl_text = (70, 0, 0)
        # window settings
        self.window = pygame.Surface((0, 0))
        self.window_size = (840, 600)
        self.window_caption = 'Labyrinth'
        # texts settings:
        self.text1_midtop = (420, 250)
        self.text2_midtop = (420, 350)
        self.text1_string = 'Press SPACE to start'
        self.text2_string = 'Press ESC to exit'
        self.font = pygame.font.Font('fonts/purisa.ttf', 40)
        pygame.display.set_caption(self.window_caption)

    def run(self):
        text1 = self.font.render(self.text1_string, True, self.cl_text)
        text1_pos = text1.get_rect()
        text1_pos.midtop = self.text1_midtop
        text2 = self.font.render(self.text2_string, True, self.cl_text)
        text2_pos = text2.get_rect()
        text2_pos.midtop = self.text2_midtop
        window = pygame.display.set_mode(self.window_size)
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
            pygame.draw.rect(window, self.cl_back_ground, (0, 0, 840, 600))
            window.blit(text1, text1_pos)
            window.blit(text2, text2_pos)
            pygame.display.update()
        pygame.quit()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    m = Menu()
    m.run()
