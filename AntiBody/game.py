import pygame
from pygame.locals import *
import sys
import os

import background as bg, laser, player

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

# define display surface
width, height = 1280, 720

os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((width, height))
pygame.display.set_caption("Antibody - Scrolling Background")
FPS = 120

# define colours
BLACK = (0,0,0,255)

# Sprites & Images
bgImage = pygame.image.load("background.png").convert()
playerImage = pygame.image.load("Player1Ship.png").convert()
laserImage = pygame.image.load("LaserGreen.png").convert()

player.x = playerImage.get_rect().width
player.y = bgImage.get_rect().height / 2


def input():
    # Keyboard input
    k = pygame.key.get_pressed()

    player.input()

    if k[K_SPACE] and not laser.active:
        laser.active = True
        laser.x = player.x
        laser.y = player.y + (playerImage.get_rect().height / 2)   # Fire from center of ships height


def move():
    # Scrolling Background
    rel_x = bg.x % bgImage.get_rect().width
    DS.blit(bgImage, (rel_x - bgImage.get_rect().width, 0))
    if rel_x < width:
        DS.blit(bgImage, (rel_x, 0))
    bg.move()

    # Laser
    laser.move()
    if laser.active:
        DS.blit(laserImage, (laser.x, laser.y))

    # Player
    player.move()
    DS.blit(playerImage, (player.x, player.y))


# Game loop
while True:
    events()
    input()
    move()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
