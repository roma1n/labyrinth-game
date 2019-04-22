import pygame


def move_possible(pos, labyrinth, direction, lab_solver):
    dirs = {'left': pos.left,
            'right': pos.right,
            'up': pos.up,
            'down': pos.down}
    return lab_solver.is_space(labyrinth, dirs[direction]())


def move(pos, labyrinth, direction, lab_solver):
    if move_possible(pos, labyrinth, direction, lab_solver):
        if direction == 'left':
            pos = pos.left()
        elif direction == 'right':
            pos = pos.right()
        elif direction == 'up':
            pos = pos.up()
        elif direction == 'down':
            pos = pos.down()
    return pos


def action(pos, labyrinth, key, lab_solver):
    if key == key_up:
        pos = move(pos, labyrinth, 'up', lab_solver)
    elif key == key_down:
        pos = move(pos, labyrinth, 'down', lab_solver)
    elif key == key_left:
        pos = move(pos, labyrinth, 'left', lab_solver)
    elif key == key_right:
        pos = move(pos, labyrinth, 'right', lab_solver)
    return pos


# set control keys
key_up = pygame.K_w
key_down = pygame.K_s
key_left = pygame.K_a
key_right = pygame.K_d
key_escape = pygame.K_ESCAPE
key_start_play = pygame.K_SPACE
