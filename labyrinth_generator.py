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

        def go_to(x, y):
            nonlocal processed
            nonlocal stack
            nonlocal a
            is_space = labyrinth_controller.is_space
            if not is_space(a, (2 * x + 1, 2 * y + 1)) or processed[x][y]:
                return False
            stack.append((x, y))
            processed[x][y] = True
            return True

        def go_up(x, y):
            nonlocal a
            if not go_to(x, y - 1):
                return False
            a[2 * x + 1][2 * y] = 0
            return True

        def go_down(x, y):
            nonlocal a
            if not go_to(x, y + 1):
                return False
            a[2 * x + 1][2 * y + 2] = 0
            return True

        def go_left(x, y):
            nonlocal a
            if not go_to(x - 1, y):
                return False
            a[2 * x][2 * y + 1] = 0
            return True

        def go_right(x, y):
            nonlocal a
            if not go_to(x + 1, y):
                return False
            a[2 * x + 2][2 * y + 1] = 0
            return True

        stack.append((0, 0))
        processed[0][0] = True
        while len(stack) > 0:
            d = [go_up, go_down, go_left, go_right]
            random.shuffle(d)
            pos_x = stack[-1][0]
            pos_y = stack[-1][1]
            if d[0](pos_x, pos_y) or d[1](pos_x, pos_y) or d[2](pos_x, pos_y) or d[3](pos_x, pos_y):
                continue
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
