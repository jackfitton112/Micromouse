import pygame
import random
(width, height) = (300, 300)
screen = pygame.display.set_mode((width, height))


def gen():


    start = (10,10)
    end = (290,290)
    list = [(start)]
    newstart = (10,10)
    while True:


        x = random.randrange(newstart[0],end[0])
        y = random.randrange(newstart[1],end[1])

        x = round(x/10)*10
        y = round(y/10)*10

        newstart = (x,y)
        list.append((x,y))

        if newstart[0] > 280 or newstart[1] > 280:
            list.append((290,290))
            break

    return list


def mazegen(width, height):

    interval = 20
    stage = 20
    while True:


        y = random.randrange(0, height-10)

        pygame.draw.line(screen, (0,0,0), (stage, 0), (stage, y), 5)
        y += 20
        pygame.draw.line(screen, (0,0,0), (stage, y), (stage, width) , 5)
        stage += 20


        if stage == 300:
            break
