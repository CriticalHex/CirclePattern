import pygame
import math
import random
pygame.init()

circleX = 400
circleY = 400
radius = 100
newCircleX = 400
newCircleY = 400

screen = pygame.display.set_mode((1000,800))

pygame.display.set_caption("Circle Drawing")

doExit = False

clock = pygame.time.Clock()

clock.tick(60)

lightBlue = (100,100,255)

degrees = 60

step = 0

depth = 2

def circles(xPos,yPos,radius,step,number):
        radians = step * (math.pi/180)
        print(radians)
        moveX = (radius * math.cos(radians))
        moveY = (radius * math.sin(radians))

        return (circleX + moveX, circleY + moveY)

pygame.draw.circle(screen, lightBlue, [circleX, circleY], radius, 1)

for y in range(depth):
    for x in range(6 * (y + 1)):
            (newCircleX, newCircleY) = circles(newCircleX, newCircleY, radius, step, x)
            pygame.draw.circle(screen, lightBlue, [newCircleX, newCircleY], 100, 1)
            step += degrees
            pygame.display.flip()
    

while doExit == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
pygame.quit()