import pygame
(width, height) = (300, 300)
screen = pygame.display.set_mode((width, height))

def convert(list):
    direction = ["N","E","S","W"]
    directionlistpos = 2

    x, y = (10, 10)
    startpos = (x, y)
    pathlist = []
    i = 0

    while i < len(list):

        if "F" in list[i]:
            if directionlistpos > 3:
                directionlistpos = directionlistpos % 4
            for j in range(int(list[i][:-1])):
                pathlist.append(direction[directionlistpos])

        else:
            if list[i] == "L":
                directionlistpos -= 1
            else:
                directionlistpos += 1

        i += 1
    return pathlist

def makepath(list):
    pathlist = convert(list)


    startpos = (10, 10)
    x, y = startpos
    finallist = [(startpos)]

    i = 0

    while i < len(pathlist):

        if pathlist[i] == "N":
            y -= 10
            finallist.append((x,y))

        elif pathlist[i] == "E":
            x -= 10
            finallist.append((x,y))

        elif pathlist[i] == "S":
            y += 10
            finallist.append((x,y))

        else:
            x += 10
            finallist.append((x,y))

        i += 1
    return finallist

def draw(start, end):
    pygame.draw.line(screen, (0,255,0), start, end, 5)

def run(list):
    #j = makepath(list)
    j = list
    i = 0

    while i < len(j):
        if i == 0:
            draw((0,0),(0,0))
        else:
            draw((j[i-1][0],j[i-1][1]),(j[i][0],j[i][1]))
        i += 1
