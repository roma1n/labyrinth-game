import labyrinth_generator
import pygame
import time
import labyrinth_controller
import player_controller
from player_controller import key_escape


def draw_frame(window, labyrinth, player):
    block_size = 40
    # define colors
    cl_wall = (100, 100, 255)
    cl_space = (200, 200, 200)
    cl_start = (200, 200, 100)
    cl_finish = (200, 50, 50)
    cl_player = (255, 255, 0)
    cl_visited = (255, 255, 120)
    color = {
        0: cl_space,
        'v': cl_visited,
        's': cl_start,
        'f': cl_finish,
        'player': cl_player,
        1: cl_wall
    }

    def draw_block(x, y, block_type):
        nonlocal block_size
        nonlocal color
        pygame.draw.rect(window, color[block_type], (x * block_size, y * block_size, block_size, block_size))

    for col in range(len(labyrinth)):
        for s in range(len(labyrinth[0])):
            draw_block(col, s, labyrinth[col][s])
    draw_block(player[0], player[1], 'player')
    return window


lab_generator = labyrinth_generator.LabyrinthGenerator(10, 7)


class Level:
    player = ()
    labyrinth = 0
    complete = bool()
    start = ()
    finish = ()
    step_counter = int()
    time_start = float()
    time_finish = float()

    def __init__(self):
        self.labyrinth, self.start, self.finish = lab_generator.generate()
        self.player = self.start
        self.complete = False
        self.step_counter = 0
        self.time_start = time.clock()

    def visit_pos(self, pos):
        self.step_counter += 1
        if pos == self.finish:
            self.complete = True
        if pos != self.start:
            self.labyrinth[pos[0]][pos[1]] = 'v'

    def time_taken(self):
        return round(self.time_finish - self.time_start, 3)

    def finish_log(self):
        self.time_finish = time.clock()
        w = labyrinth_controller.optimal_way_length(self.labyrinth, self.start, self.finish)
        score = round(100 * w / self.step_counter, 1)
        print("You've done in {} steps".format(self.step_counter))
        print("Your way was optimal for {}%".format(score))
        print("Time taken: {}".format(self.time_taken()))


class Game:
    def play(self, window):
        run = True
        level = Level()
        while run:
            if level.complete:
                level.__init__()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.KEYDOWN:
                    if event.key == key_escape:
                        return False
                    previous_pos = level.player
                    level.player = player_controller.action(level.player, level.labyrinth, event.key)
                    if previous_pos != level.player:
                        level.visit_pos(level.player)
            window = draw_frame(window, level.labyrinth, level.player)
            pygame.display.update()
            if level.complete:
                level.finish_log()
        return False
