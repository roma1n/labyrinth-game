import pygame
import game


def move_possible(pos, labyrinth, direction):
    dirs = {'left': pos.left,
            'right': pos.right,
            'up': pos.up,
            'down': pos.down}
    return game.lab_solver.is_space(labyrinth, dirs[direction]())


def move(pos, labyrinth, direction):
    if move_possible(pos, labyrinth, direction):
        if direction == 'left':
            pos = pos.left()
        elif direction == 'right':
            pos = pos.right()
        elif direction == 'up':
            pos = pos.up()
        elif direction == 'down':
            pos = pos.down()
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
