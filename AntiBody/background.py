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

# define colours
BLACK = (0,0,0,255)
WHITE = (255,255,255,255)

# Sprites & Images
bgImage = pygame.image.load("background.png").convert()
playerImage = pygame.image.load("Player1Ship.png").convert()
laserImage = pygame.image.load("LaserGreen.png").convert()

x = 0

circleRadius = 25
circlePosX = circleRadius

playerPosX = circleRadius
playerPosY = 585
playerVelocityX, playerVelocityY = 0, 0

laserX, laserY = 0,0
laserActive = False

SPEED = 5

# main loop
while True:
    events()

    # Scrolling Background
    rel_x = x % bgImage.get_rect().width
    DS.blit(bgImage, (rel_x - bgImage.get_rect().width, 0))
    if rel_x < width:
        DS.blit(bgImage, (rel_x, 0))
    x -= 1

    # Keyboard input
    k = pygame.key.get_pressed()
    if k[K_RIGHT]:
        playerVelocityX = 1
    elif k[K_LEFT]:
        playerVelocityX = -1
    else:
        playerVelocityX = 0

    if k[K_UP]:
        playerVelocityY = -1
    elif k[K_DOWN]:
        playerVelocityY = 1
    else:
        playerVelocityY = 0

    if k[K_SPACE] and not laserActive:
        laserActive = True
        laserX = playerPosX
        laserY = playerPosY + (playerImage.get_rect().height / 2)   # Fire from center of ships height


    # Laser
    if laserActive:
        laserX += 10
        DS.blit(laserImage, (laserX, laserY))
        if laserX > width:
            laserActive = False


    # Update Player Position
    playerPosX += playerVelocityX * SPEED
    playerPosY += playerVelocityY * SPEED

    # pygame.draw.circle(DS, WHITE, (playerPosX, playerPosY - circleRadius), circleRadius, 0)
    DS.blit(playerImage, (playerPosX, playerPosY))


    # pygame.draw.line(DS, 255,0,0), (rel_x, 0)
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
