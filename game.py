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
        for row in range(len(labyrinth[0])):
            draw_block(col, row, labyrinth[col][row])
    draw_block(player.x, player.y, 'player')
    return window


lab_generator = labyrinth_generator.LabyrinthGenerator(10, 7)
lab_solver = labyrinth_controller.LabyrinthSolver(10, 7)


class Level:
    def __init__(self):
        self.labyrinth, self.start, self.finish = lab_generator.generate()
        self.player = self.start
        self.complete = False
        self.step_counter = 0
        self.time_start = time.clock()
        self.time_finish = None

    def visit_pos(self, pos):
        self.step_counter += 1
        if pos == self.finish:
            self.complete = True
        if pos != self.start:
            self.labyrinth[pos.x][pos.y] = 'v'

    def time_taken(self):
        return round(self.time_finish - self.time_start, 3)

    def finish_log(self):
        self.time_finish = time.clock()
        labyrinth_solver = labyrinth_controller.LabyrinthSolver(10, 7)
        w = labyrinth_solver.optimal_way_length(self.labyrinth, self.start, self.finish)
        score = round(100 * w / self.step_counter, 1)
        print("You've done in {} steps".format(self.step_counter))
        print("Your way was optimal for {}%".format(score))
        print("Time taken: {}".format(self.time_taken()))


class Game:
    def __init__(self):
        self.level = Level()

    def complete_level(self):
        self.level.finish_log()

    def start_level(self):
        self.level = Level()

    def update(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == key_escape:
                    return False
                previous_pos = self.level.player
                self.level.player = player_controller.action(self.level.player, self.level.labyrinth, event.key)
                if previous_pos != self.level.player:
                    self.level.visit_pos(self.level.player)
        draw_frame(window, self.level.labyrinth, self.level.player)
        pygame.display.update()
        return None

    def play(self, window):
        run = True
        while run:
            if self.level.complete:
                self.start_level()
            exit_event_type = self.update(window)
            if exit_event_type is not None:
                return exit_event_type
            if self.level.complete:
                self.complete_level()
        return False
