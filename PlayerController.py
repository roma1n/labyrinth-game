import LabirintGenerator
import LabirintController


def MovePossible(pos, labirint, direction):
    if direction == 'left':
        if LabirintController.IsSpace(labirint, (pos[0] - 1, pos[1])):
            return True
    elif direction == 'right':
        if LabirintController.IsSpace(labirint, (pos[0] + 1, pos[1])):
            return True
    elif direction == 'up':
        if LabirintController.IsSpace(labirint, (pos[0], pos[1] - 1)):
            return True
    elif direction == 'down':
        if LabirintController.IsSpace(labirint, (pos[0], pos[1] + 1)):
            return True
    return False


def Move(pos, labirint, direction):
    if MovePossible(pos, labirint, direction):
        if direction == 'left':
            pos = (pos[0] - 1, pos[1])
        elif direction == 'right':
            pos = (pos[0] + 1, pos[1])
        elif direction == 'up':
            pos = (pos[0], pos[1] - 1)
        elif direction == 'down':
            pos = (pos[0], pos[1] + 1)
    return pos


def Action(pos, labirint, key):
    key = chr(key)
    if key == keyUp:
        pos = Move(pos, labirint, 'up')
    elif key == keyDown:
        pos = Move(pos, labirint, 'down')
    elif key == keyLeft:
        pos = Move(pos, labirint, 'left')
    elif key == keyRight:
        pos = Move(pos, labirint, 'right')
    return pos


# set control keys
keyUp = 'w'
keyDown = 's'
keyLeft = 'a'
keyRight = 'd'
