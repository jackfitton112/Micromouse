#imports pygame, used to trace the path of mouse
import pygame


##LIST RECIEVED FROM ESP
list = ["FD","FD","R90","FD","FD","FD","FD","FD","FD","L90","FD","FD","FD"]

#defines window width and baclground colour
(width, height) = (300, 300)
background_colour = (255,255,255)

#initalizes screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Micromouse Tracer')
screen.fill(background_colour)

def draw(start, end):
    pygame.draw.line(screen, (0,0,0), start, end, 5)

def convert(list):
    calcdlist = []
    i = 0
    while i < len(list):
        if list[i] == "FD":
            calcdlist.append(10)
        elif list[i] == "R90":
            calcdlist.append(-90)
        elif list[i] == "L90":
            calcdlist.append(90)
        i += 1
    return calcdlist

def makepath(list):
    pathlist = convert(list) #converts list into path
    x, y = (150,150)
    path = [(x,y)]
    current = "y"
    degree = 0


    i = 0

    while i < len(pathlist):

        if pathlist[i] == 10:

            if current == "y" and degree > 90:
                y += 10
                path.append((x,y))

            elif current == "x" and degree > 90:
                x += 10
                path.append((x,y))

            elif current == "y" and degree <= 90:
                y -= 10
                path.append((x,y))

            elif current == "x" and degree <= 90:
                x -= 10
                path.append((x,y))

        else:

            degree += pathlist[i]


        i += 1
    return path


j = makepath(list)
i = 0
print(j)
while i < len(j):
    if i == 0:
        draw((150,150),(150,150))
    else:
        draw((j[i-1][0],j[i-1][1]),(j[i][0],j[i][1]))
    i += 1

#flips display for correct orientation
pygame.display.flip()


#allows the user to press red x to exit program
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
