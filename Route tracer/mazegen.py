import random
import pygame
size = (20, 20)
coords = [(0, 0)] # will contain [(x, y), (x, y)] of already passed nodes
paths = [] # will contain [((xa, ya), (xb, yb)), (...)] of paths
screen = pygame.display.set_mode((size[0]*10, size[1]*10))

#   0
#  3 1
#   2
#  x-->
# y
# |
# V
def draw(start, end):
    pygame.draw.line(screen, (0,255,0), (start[0]*10, start[1]*10), (end[0]*10, end[1]*10), 3)

def checkPath(place, direction): # check if path valid
    target = getTarget(place, direction)
    if (target[0] < 0) or (target[1] < 0): # outside min bounds
        return False
    elif (target[0] > size[0]) or (target[1] > size[1]): #outside max bounds
        return False
    elif target in coords: # node already visited
        return False
    else:
        return True

def getTarget(start, direction): # maths to see where it is going
    if direction == 0:
        return (start[0], start[1]-1)
    elif direction == 1:
        return (start[0]+1, start[1])
    elif direction == 2:
        return (start[0], start[1]+1)
    else:
        return (start[0]-1, start[1])

for place in coords:
    for n in range(0, 3):
        if random.randint(0, 4):
            if checkPath(place, n):
                paths.append((place, getTarget(place, n)))
                coords.append(getTarget(place, n))


for path in paths:
    draw(path[0], path[1])
pygame.display.flip()
