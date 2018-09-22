import pygame
from pygame.locals import *
import sys
import os

import background as bg, laser, player, bloodcell


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
bgImage = pygame.image.load("Art/background.png").convert()
playerImage = pygame.image.load("Art/Player1Ship.png").convert()
laserImage = pygame.image.load("Art/LaserGreen.png").convert()
bloodcellImage = pygame.image.load("Art/BloodCell.png").convert()
orig_image = bloodcellImage

# Audio
laserFX = pygame.mixer.Sound('Audio/laser1.wav')
explosionFX = pygame.mixer.Sound('Audio/explosion.wav')

player.x = playerImage.get_rect().width
player.y = bgImage.get_rect().height / 2
bloodcell.x = 500
bloodcell.y = 360


def input():
    # Keyboard input
    k = pygame.key.get_pressed()

    player.input()

    if k[K_SPACE] and not laser.active:
        laser.active = True
        laser.x = player.x
        laser.y = player.y + (playerImage.get_rect().height / 2)   # Fire from center of ships height
        laserFX.play()


def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    # Rotate the original image without modifying it.
    new_image = pygame.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect.
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect


def move():
    global bloodcellImage

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
    if laser.explosion:
        explosionFX.play()
        laser.explosion = False
        bloodcell.x = 1280

    # Player
    player.move()
    DS.blit(playerImage, (player.x, player.y))

    # BloodCell
    rect = bloodcellImage.get_rect(center=(bloodcell.x,bloodcell.y))
    bloodcell.move()

    bloodcellImage, rect = rotate(orig_image, rect, bloodcell.angle)
    DS.blit(bloodcellImage, rect)

    laser.collisions(rect)
    # laser.collisions2(bloodcell.x, bloodcell.y, bloodcell.width, bloodcell.height)


# Game loop
while True:
    events()
    input()
    move()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
