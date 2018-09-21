import pygame
from pygame.locals import *
import sys
import os

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

# define display surface
width, height = 1280, 720
#HW, HH = width / 2, height / 2
#AREA = width * height

os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((width, height))
pygame.display.set_caption("Antibody - Scrolling Background")
FPS = 120

bgImage = pygame.image.load("background.png").convert()
x = 0

# main loop
while True:
    events()

    rel_x = x % bgImage.get_rect().width
    DS.blit(bgImage, (rel_x - bgImage.get_rect().width, 0))
    if rel_x < width:
        DS.blit(bgImage, (rel_x, 0))
    x -= 1

    #pygame.draw.line(DS, 255,0,0), (rel_x, 0)
    pygame.display.update()
    CLOCK.tick(FPS)
