import random
import labyrinth_controller
import game


class LabyrinthGenerator:
    """
    This class generates labyrinth
    Takes length, height
    Method generate() returns matrix (2 * length + 1) x (2 * height + 1)
    Algorithm using for generation: DFS with random choice of
    next point among vertices that are next to current
    Result: tree
    """

    def __init__(self, length, height):
        self.height = height
        self.length = length

    def generate_clear_field(self):
        return [[1 - (i % 2) * (j % 2) for j in range(2 * self.height + 1)] for i in range(2 * self.length + 1)]

    def make_ways(self, labyrinth):
        processed = [[False for j in range(self.height)] for i in range(self.length)]
        stack = []

        def is_available(pos):
            return game.lab_solver.is_space(labyrinth, pos) and not processed[pos.x // 2][pos.y // 2]

        def get_available_directions(pos):
            dirs = {
                pos.left().left(): 'left',
                pos.up().up(): 'up',
                pos.right().right(): 'right',
                pos.down().down(): 'down'
            }
            res = []
            for direction in dirs:
                if is_available(direction):
                    res.append(dirs[direction])
            return res

        stack.append(labyrinth_controller.Position(1, 1))
        processed[0][0] = True
        while len(stack) > 0:
            cur_pos = stack[-1]
            avail_dirs_str = get_available_directions(cur_pos)
            if len(avail_dirs_str) > 0:
                random.shuffle(avail_dirs_str)
                wall_to_destroy = cur_pos.next_by_str(avail_dirs_str[0])()
                labyrinth[wall_to_destroy.x][wall_to_destroy.y] = 0
                new_pos = wall_to_destroy.next_by_str(avail_dirs_str[0])()
                stack.append(new_pos)
                processed[new_pos.x // 2][new_pos.y // 2] = True
            else:
                stack.pop()
        return labyrinth

    def get_random_point(self):
        x = random.choice(range(self.length))
        y = random.choice(range(self.height))
        return labyrinth_controller.Position(2 * x + 1, 2 * y + 1)

    def set_way(self, labyrinth):
        start = self.get_random_point()
        finish = self.get_random_point()
        while finish == start:
            finish = self.get_random_point()
        labyrinth[start.x][start.y] = 's'
        labyrinth[finish.x][finish.y] = 'f'
        return start, finish

    def generate(self):
        res = self.make_ways(self.generate_clear_field())
        start, finish = self.set_way(res)
        return res, start, finish
