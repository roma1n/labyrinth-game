from collections import deque


def optimal_way_length(labyrinth, start, finish):
    """
    This function returns way from start to finish length
    Uses algorithms: bfs
    """
    bfs_queue = deque()
    sizes = (len(labyrinth[0]), len(labyrinth))
    used = [[False for j in range(sizes[0])] for i in range(sizes[1])]

    def go_to(way_length, new_pos):
        nonlocal used
        nonlocal labyrinth
        nonlocal bfs_queue
        x = new_pos[0]
        y = new_pos[1]
        if is_space(labyrinth, new_pos) and not used[x][y]:
            used[x][y] = True
            bfs_queue.append((way_length, new_pos))

    bfs_queue.append((0, start))
    while len(bfs_queue) > 0:
        pos = bfs_queue[0]
        bfs_queue.popleft()
        if pos[1] == finish:
            return pos[0]
        go_to(pos[0] + 1, (pos[1][0] + 1, pos[1][1]))
        go_to(pos[0] + 1, (pos[1][0] - 1, pos[1][1]))
        go_to(pos[0] + 1, (pos[1][0], pos[1][1] + 1))
        go_to(pos[0] + 1, (pos[1][0], pos[1][1] - 1))
    return None


def is_space(labyrinth, pos):
    ok_horizontal = 0 <= pos[0] < len(labyrinth)
    ok_vertical = 0 <= pos[1] < len(labyrinth[0])
    if ok_horizontal and ok_vertical and not labyrinth[pos[0]][pos[1]] == 1:
        return True
    return False
