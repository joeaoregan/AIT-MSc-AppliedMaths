import pygame
from pygame.locals import *

# define display surface
width, height = 1280, 720
x = 0


def move():
    global x
    x -= 1
