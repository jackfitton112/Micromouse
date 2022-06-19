#imports pygame, used to trace the path of mouse
import pygame

#defines window width and baclground colour
(width, height) = (300, 300)
background_colour = (255,255,255)

#initalizes screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Micromouse Tracer')
screen.fill(background_colour)


##LIST RECIEVED FROM ESP

list = ["10F","R","1F","R","5F","L","15F"]

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
    pygame.draw.line(screen, (0,0,0), start, end, 5)


def run(list):
    j = makepath(list)
    i = 0

    while i < len(j):
        if i == 0:
            draw((150,150),(150,150))
        else:
            draw((j[i-1][0],j[i-1][1]),(j[i][0],j[i][1]))
        i += 1


run(list)


#flips display for correct orientation
pygame.display.flip()
#allows the user to press red x to exit program
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False





















#flips display for correct orientation
pygame.display.flip()


#allows the user to press red x to exit program
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
