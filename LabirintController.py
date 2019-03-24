import LabirintGenerator
from collections import deque


def FindStart(labirint):
	for col in range(len(labirint)):
		for line in range(len(labirint[0])):
			if labirint[col][line] == 's':
				return (col, line)
	return False


def FindFinish(labirint):
	for col in range(len(labirint)):
		for line in range(len(labirint[0])):
			if labirint[col][line] == 'f':
				return (col, line)
	return False


def OptimalWayLength(labirint, start, finish):
	q = deque()
	used = [[False for j in range(len(labirint[0]))] for i in range(len(labirint))]

	def GoTo(wayLength, pos):
		nonlocal used
		nonlocal labirint
		nonlocal q
		x = pos[0]
		y = pos[1]
		if IsSpace(labirint, pos) and not used[x][y]:
			used[x][y] = True
			q.append((wayLength, pos))

	q.append((0, start))
	while len(q) > 0:
		p = q[0]
		q.popleft()
		if p[1] == finish:
			return p[0]
		GoTo(p[0] + 1, (p[1][0] + 1, p[1][1]))
		GoTo(p[0] + 1, (p[1][0] - 1, p[1][1]))
		GoTo(p[0] + 1, (p[1][0], p[1][1] + 1))
		GoTo(p[0] + 1, (p[1][0], p[1][1] - 1))
	return False


def IsSpace(l, pos):
	if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(l) and pos[1] < len(l[0]) and not l[pos[0]][pos[1]] == 1:
		return True
	return False
