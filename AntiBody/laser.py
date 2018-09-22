import pygame
from pygame.locals import *
import background

x, y = 0,0
active = False


def init():
    global x, y
    global active
    x, y = 0, 0
    active = False


def move():
    global active, x
    if active:
        x += 10

        if x > background.width:
            active = False
