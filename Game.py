import LabirintGenerator
import pygame
import time
import LabirintController
import PlayerController


def DrawFrame(window, labirint, plPos):
    size = 40
    # define colors
    clWall = (100, 100, 255)
    clSpace = (200, 200, 200)
    clStart = (200, 200, 100)
    clFinish = (200, 50, 50)
    clPlayer = (255, 255, 0)
    clVisited = (255, 255, 120)

    def DrawSection(x, y, type):
        nonlocal size
        color = (0, 0, 0)
        if type == 0:
            color = clSpace
        elif type == 'v':
            color = clVisited
        elif type == 's':
            color = clStart
        elif type == 'f':
            color = clFinish
        elif type == 'player':
            color = clPlayer
        else:
            color = clWall
        pygame.draw.rect(window, color, (x * size, y * size, size, size))

    for col in range(len(labirint)):
        for s in range(len(labirint[0])):
            DrawSection(col, s, labirint[col][s])
    DrawSection(plPos[0], plPos[1], 'player')
    return window


def RestartLevel():
    labirint = LabirintGenerator.GenerateLabirint(10, 7)
    labirint = LabirintGenerator.SetWay(labirint)
    playerPosition = LabirintController.FindStart(labirint)
    finishPosition = LabirintController.FindFinish(labirint)
    return (labirint, playerPosition, finishPosition)


def Game(window):
    run = True
    pPos = 0
    labirint = 0
    complete = True
    sPos = 0
    fPos = 0
    stepCounter = 0
    fullExit = False
    while run:
        if complete:
            newLevel = RestartLevel()
            labirint = newLevel[0]
            sPos = newLevel[1]
            fPos = newLevel[2]
            pPos = sPos
            stepCounter = 0
            complete = False
            timeStart = time.clock()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                fullExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == 27:
                    run = False
                    fullExit = False
                prePos = pPos
                pPos = PlayerController.Action(pPos, labirint, event.key)
                if prePos != pPos:
                    if pPos != sPos:
                        labirint[pPos[0]][pPos[1]] = 'v'
                    stepCounter += 1
                    if pPos == fPos:
                        complete = True
        window = DrawFrame(window, labirint, pPos)
        pygame.display.update()
        if complete:
            timeFinish = time.clock()
            print("You've done in {} steps".format(stepCounter))
            w = LabirintController.OptimalWayLength(labirint, sPos, fPos)
            score = round(100*w/stepCounter, 1)
            print("Your way was optimal for {}%".format(score))
            timeTaken = round(timeFinish - timeStart, 3)
            print("Time taken: {}".format(timeTaken))
    return fullExit
