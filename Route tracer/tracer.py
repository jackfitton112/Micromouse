#imports pygame, used to trace the path of mouse
import pygame
from functions import convert
from functions import makepath
from functions import draw
from functions import run
from routegen import gen
from routegen import mazegen
#defines window width and baclground colour
(width, height) = (300, 300)
background_colour = (255,255,255)

#initalizes screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Micromouse Tracer')
screen.fill(background_colour)


##LIST RECIEVED FROM ESP
list = gen()
print(list)
#start
pygame.draw.circle(screen, (0,128,0), (10,10), 10, 5)
#end
pygame.draw.circle(screen, (255,0,0), (290,290), 10, 5)

run(list)
mazegen(300,300)
#flips display for correct orientation
pygame.display.flip()




#allows the user to press red x to exit program
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
