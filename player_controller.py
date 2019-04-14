import pygame
import labyrinth_controller


def move_possible(pos, labyrinth, direction):
    dirs = {'left': (pos[0] - 1, pos[1]),
            'right': (pos[0] + 1, pos[1]),
            'up': (pos[0], pos[1] - 1),
            'down': (pos[0], pos[1] + 1)}
    return labyrinth_controller.is_space(labyrinth, dirs[direction])


def move(pos, labyrinth, direction):
    if move_possible(pos, labyrinth, direction):
        if direction == 'left':
            pos = (pos[0] - 1, pos[1])
        elif direction == 'right':
            pos = (pos[0] + 1, pos[1])
        elif direction == 'up':
            pos = (pos[0], pos[1] - 1)
        elif direction == 'down':
            pos = (pos[0], pos[1] + 1)
    return pos


def action(pos, labyrinth, key):
    if key == key_up:
        pos = move(pos, labyrinth, 'up')
    elif key == key_down:
        pos = move(pos, labyrinth, 'down')
    elif key == key_left:
        pos = move(pos, labyrinth, 'left')
    elif key == key_right:
        pos = move(pos, labyrinth, 'right')
    return pos


# set control keys
key_up = pygame.K_w
key_down = pygame.K_s
key_left = pygame.K_a
key_right = pygame.K_d
key_escape = pygame.K_ESCAPE
key_start_play = pygame.K_SPACE
