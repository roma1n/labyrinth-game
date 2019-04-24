from collections import deque


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        return Position(self.x, self.y - 1)

    def down(self):
        return Position(self.x, self.y + 1)

    def left(self):
        return Position(self.x - 1, self.y)

    def right(self):
        return Position(self.x + 1, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def next_by_str(self, s):
        str_to_func = {
            'left': self.left,
            'right': self.right,
            'up': self.up,
            'down': self.down
        }
        return str_to_func[s]

    def __hash__(self):
        return (13 * self.x.__hash__()) ^ (239 * self.y.__hash__())


class LabyrinthSolver:
    def __init__(self, length, height):
        self.sizes = Position(2 * length + 1, 2 * height + 1)

    def optimal_way_length(self, labyrinth, start, finish):
        """
        This function returns way from start to finish length
        Uses algorithms: bfs
        """
        bfs_queue = deque()
        used = [[False for j in range(self.sizes.y)] for i in range(self.sizes.x)]

        def go_to(way_length, new_pos):
            nonlocal used
            nonlocal labyrinth
            nonlocal bfs_queue
            x = new_pos.x
            y = new_pos.y
            if self.is_space(labyrinth, new_pos) and not used[x][y]:
                used[x][y] = True
                bfs_queue.append((way_length, new_pos))

        bfs_queue.append((0, start))
        while len(bfs_queue) > 0:
            way_len, pos = bfs_queue[0]
            bfs_queue.popleft()
            if pos == finish:
                return way_len
            go_to(way_len + 1, pos.right())
            go_to(way_len + 1, pos.left())
            go_to(way_len + 1, pos.down())
            go_to(way_len + 1, pos.up())
        return None

    def is_space(self, labyrinth, pos):
        ok_horizontal = 0 <= pos.x < self.sizes.x
        ok_vertical = 0 <= pos.y < self.sizes.y
        if ok_horizontal and ok_vertical and not labyrinth[pos.x][pos.y] == 1:
            return True
        return False
