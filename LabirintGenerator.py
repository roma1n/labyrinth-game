import random
import LabirintController


def GenerateLabirint(length, height):
	'''
	This function generates labirint
	Takes length, height
	Returns matrix (2 * lenght + 1) x (2 * hegiht + 1)
	Algorithm using for generation: DFS with random choice of
	next point among vertices that are next to current
	Result: tree
	'''

	def GenerateClearField():
		nonlocal length
		nonlocal height
		a = [[1 for j in range(2 * height + 1)] for i in range(2 * length + 1)]
		for i in range(length):
			for j in range(height):
				a[2 * i + 1][2 * j + 1] = 0
		return a

	def MakeWays(a):
		nonlocal length
		nonlocal height
		processed = [[False for j in range(height)] for i in range(length)]
		stack = []

		def GoTo(x, y):
			nonlocal processed
			nonlocal stack
			nonlocal a
			if  not LabirintController.IsSpace(a, (2 * x + 1, 2 * y + 1)) or processed[x][y]:
				return False
			stack.append((x, y))
			processed[x][y] = True
			return True

		def GoUp(x, y):
			nonlocal a
			if not GoTo(x, y - 1):
				return False
			
			a[2 * x + 1][2 * y] = 0
			
			return True

		def GoDown(x, y):
			nonlocal a
			if not GoTo(x, y + 1):
				return False
			
			a[2 * x + 1][2 * y + 2] = 0
			return True

		def GoLeft(x, y):
			nonlocal a
			if not GoTo(x - 1, y):
				return False
			a[2 * x][2 * y + 1] = 0
			return True

		def GoRight(x, y):
			nonlocal a
			if not GoTo(x + 1, y):
				return False
			a[2 * x + 2][2 * y + 1] = 0
			return True

		stack.append((0, 0))
		processed[0][0] = True
		while len(stack) > 0:
			dirs = [GoUp, GoDown, GoLeft, GoRight]
			random.shuffle(dirs)
			x = stack[-1][0]
			y = stack[-1][1]
			if dirs[0](x, y) or dirs[1](x, y) or dirs[2](x, y) or dirs[3](x, y):
				continue
			stack.pop()
		return a

	res = MakeWays(GenerateClearField())
	return res


def GetRandomPoint(labirint):
	x = random.choice(range(len(labirint) // 2)[1:-1])
	y = random.choice(range(len(labirint[0]) // 2)[1:-1])
	return (2 * x + 1, 2 * y + 1)


def SetWay(labirint):
	start = GetRandomPoint(labirint)
	finish = GetRandomPoint(labirint)
	while finish == start:
		finish = GetRandomPoint(labirint)
	labirint[start[0]][start[1]] = 's'
	labirint[finish[0]][finish[1]] = 'f'
	return labirint


def PrintLabirint(a):
	for line in a:
		print(*line, sep='')
