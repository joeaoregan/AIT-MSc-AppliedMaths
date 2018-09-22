import pygame
from pygame.locals import *
import sys
import os

import AntiBody.bullet as bullet
import background as bg, AntiBody.laser as laser, AntiBody.player as player, AntiBody.bloodcell as bloodcell
import AntiBody.object as object

print("Test")


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

# objectImage = pygame.image.load("Art/Player1Ship.png").convert()
player1 = player.Player(playerImage.get_rect().width, bgImage.get_rect().height / 2)
bloodCell1 = bloodcell.BloodCell(500,360)

orig_image = bloodcellImage

# Audio
# laserFX = pygame.mixer.Sound('Audio/laser1.wav')
# explosionFX = pygame.mixer.Sound('Audio/explosion.wav')

# player.x = playerImage.get_rect().width
# player.y = bgImage.get_rect().height / 2
# bloodcell.x = 500
# bloodcell.y = 360

bulletList = pygame.sprite.Group()

# nextFire = 0

def input():
    global nextFire
    # pygame.key.set_repeat(200, 200)
    # Keyboard input
    k = pygame.key.get_pressed()

    # player.input()
    player1.input()

   # fire = pygame.time.get_ticks()

#    if k[K_SPACE] and not laser.active:
#        laser.active = True
        # laser.x = player.x
        # laser.y = player.y + (playerImage.get_rect().height / 2)   # Fire from center of ships height
#        laser.x = player1.x
#        laser.y = player1.y + (playerImage.get_rect().height / 2)
#        laserFX.play()
    if k[K_SPACE] and pygame.time.get_ticks() > bullet.NEXT_FIRE:
#        laser1 = laser.Laser(player1.x, player1.y + (playerImage.get_rect().height / 2))
        bullet1 = bullet.Bullet(player1.x, player1.y + (playerImage.get_rect().height / 2))
        bulletList.add(bullet1)
        bullet.NEXT_FIRE = pygame.time.get_ticks() + 200


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
    # laser1.move()

    #if laser.active:
    #    DS.blit(laserImage, (laser.x, laser.y))
    #if laser.explosion:
    #    explosionFX.play()
    #    laser.explosion = False
    #    bloodCell1.x = 1280


    # Player
    # player.move()
    # DS.blit(playerImage, (player.x, player.y))

    # Object
    player1.move()
    DS.blit(playerImage, (player1.x, player1.y))

    # BloodCell
    rect = bloodcellImage.get_rect(center=(bloodCell1.x,bloodCell1.y))
    bloodCell1.move()

    bloodcellImage, rect = rotate(orig_image, rect, bloodCell1.angle)
    DS.blit(bloodcellImage, rect)

    for bullets in bulletList:
        bullets.move()
        DS.blit(laserImage, (bullets.x, bullets.y))
        bullets.collisions(rect)
        if not bullets.active:
            bulletList.remove(bullets)

    # laser.collisions(rect)    # WORKS
    # laser.collisions2(bloodcell.x, bloodcell.y, bloodcell.width, bloodcell.height)


# Game loop
while True:
    events()
    input()
    move()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
