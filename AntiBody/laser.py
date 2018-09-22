import pygame
from pygame.locals import *
import background

x, y = 0,0
width, height = 100, 47
active = False
explosion = False

def init():
    global x, y
    global active
    x, y = 0, 0
    active = False


def collisions(rect):
    global explosion, active
    if x < rect.left + rect.width and x + width > rect.left and y < rect.top + rect.height and y + height > rect.top:
        explosion = True
        active = False


def collisions2(objectX,objectY,objectW,objectH):
    global explosion, active
    if x < objectX + objectW and x + width > objectX and y < objectY + objectH and y + height > objectY:
        explosion = True
        active = False


def move():
    global active, x
    if active:
        x += 10

        if x > background.width:
            active = False

    if not active:
        x,y=0,0
