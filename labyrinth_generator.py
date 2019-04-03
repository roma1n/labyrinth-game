import random
import labyrinth_controller


class LabyrinthGenerator:
    """
    This class generates labyrinth
    Takes length, height
    Method generate() returns matrix (2 * length + 1) x (2 * height + 1)
    Algorithm using for generation: DFS with random choice of
    next point among vertices that are next to current
    Result: tree
    """
    height = int()
    length = int()

    def __init__(self, _l, _h):
        self.height = _h
        self.length = _l

    def generate_clear_field(self):
        a = [[1] * (2 * self.length + 1) for i in range(2 * self.length + 1)]
        for i in range(self.length):
            for j in range(self.height):
                a[2 * i + 1][2 * j + 1] = 0
        return a

    def make_ways(self, a):
        processed = [[False for j in range(self.height)] for i in range(self.length)]
        stack = []

        def is_available(x, y):
            is_space = labyrinth_controller.is_space
            if not is_space(a, (2 * x + 1, 2 * y + 1)) or processed[x][y]:
                return False
            else:
                return True

        def get_available_directions(x, y):
            dirs = {
                (x - 1, y): 'left',
                (x, y - 1): 'up',
                (x + 1, y): 'right',
                (x, y + 1): 'down'
            }
            res = []
            for direction in dirs:
                if is_available(direction[0], direction[1]):
                    res.append(dirs[direction])
            return res

        def go_to(x, y):
            stack.append((x, y))
            processed[x][y] = True

        def go_up(x, y):
            go_to(x, y - 1)
            a[2 * x + 1][2 * y] = 0

        def go_down(x, y):
            go_to(x, y + 1)
            a[2 * x + 1][2 * y + 2] = 0

        def go_left(x, y):
            go_to(x - 1, y)
            a[2 * x][2 * y + 1] = 0

        def go_right(x, y):
            go_to(x + 1, y)
            a[2 * x + 2][2 * y + 1] = 0

        stack.append((0, 0))
        processed[0][0] = True
        dirs_str_to_funcs = {
            'left': go_left,
            'right': go_right,
            'up': go_up,
            'down': go_down
        }
        while len(stack) > 0:
            pos_x = stack[-1][0]
            pos_y = stack[-1][1]
            avail_dirs_str = get_available_directions(pos_x, pos_y)
            if len(avail_dirs_str) > 0:
                dir_funcs = []
                for dir_str in avail_dirs_str:
                    dir_funcs.append(dirs_str_to_funcs[dir_str])
                random.shuffle(dir_funcs)
                dir_funcs[0](pos_x, pos_y)
            else:
                stack.pop()
        return a

    def get_random_point(self):
        x = random.choice(range(self.length))
        y = random.choice(range(self.height))
        return 2 * x + 1, 2 * y + 1

    def set_way(self, labyrinth):
        start = self.get_random_point()
        finish = self.get_random_point()
        while finish == start:
            finish = self.get_random_point()
        labyrinth[start[0]][start[1]] = 's'
        labyrinth[finish[0]][finish[1]] = 'f'
        return start, finish

    def generate(self):
        res = self.make_ways(self.generate_clear_field())
        start, finish = self.set_way(res)
        return res, start, finish
