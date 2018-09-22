import pygame
from pygame.locals import *

x, y = 0, 0
velocityX, velocityY = 0,0

SPEED = 5


def input():
    global velocityX, velocityY
    k = pygame.key.get_pressed()
    if k[K_RIGHT]:
        velocityX = 1
    elif k[K_LEFT]:
        velocityX = -1
    else:
        velocityX = 0

    if k[K_UP]:
        velocityY = -1
    elif k[K_DOWN]:
        velocityY = 1
    else:
        velocityY = 0



def move():
    global x, y, SPEED
    x += velocityX * SPEED
    y += velocityY * SPEED

    # Keep player in window boundary
    if y < 20:
        y = 20
    elif y > 550:
        y = 550

    if x < 0:
        x = 0
    elif x > 1180:
        x = 1180
