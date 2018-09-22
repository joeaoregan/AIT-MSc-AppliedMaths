import pygame
from pygame.locals import *
import sys
import os

import AntiBody.bullet as bullet
import background as bg, AntiBody.laser as laser, AntiBody.player as player, AntiBody.bloodcell as bloodcell
import AntiBody.object as object

# print("Test")
score = 0

# font = pygame.font.SysFont("comicsansms", 24)
fontName = pygame.font.match_font("comicsansms")
def drawText(surface, text, size, x, y):
    font = pygame.font.Font(fontName, 24)
    text = font.render(text, True, (255, 255, 255))   # True = text anti-aliased
    textRect = text.get_rect()
    textRect.midtop = (x,y)
    surface.blit(text, textRect)    # draw text surface at location of text rectangle


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

player1 = player.Player(playerImage.get_rect().width, bgImage.get_rect().height / 2)
# bloodCell1 = bloodcell.BloodCell(500,360)

bulletList = pygame.sprite.Group()
bloodCellList = pygame.sprite.Group()

# nextFire = 0

def input():
    global nextFire
    # pygame.key.set_repeat(200, 200)
    # Keyboard input
    k = pygame.key.get_pressed()

    # player.input()
    player1.input()

    if k[K_SPACE] and pygame.time.get_ticks() > bullet.NEXT_FIRE:
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


def spawnBloodCells():
    if len(bloodCellList) < 8:
        # bloodCell1 = bloodcell.BloodCell(random.rand, 360)
        bloodCell1 = bloodcell.BloodCell()
        bloodCellList.add(bloodCell1)


def move():
    global bloodcellImage, score

    # Scrolling Background
    rel_x = bg.x % bgImage.get_rect().width
    DS.blit(bgImage, (rel_x - bgImage.get_rect().width, 0))
    if rel_x < width:
        DS.blit(bgImage, (rel_x, 0))
    bg.move()

    # BloodCell
    # rect = bloodcellImage.get_rect(center=(bloodCell1.x,bloodCell1.y))
    # bloodCell1.move()
    # bloodcellImage, rect = rotate(orig_image, rect, bloodCell1.angle)
    # DS.blit(bloodcellImage, rect)

    # Move and Draw Blood Cells
    for bloodCells in bloodCellList:
        bloodCells.move()
        rect = bloodcellImage.get_rect(center=(bloodCells.x,bloodCells.y))
        bloodcellImage, rect = rotate(orig_image, rect, bloodCells.angle)
        DS.blit(bloodcellImage, rect)
        if bloodCells.x < -bloodCells.width:
            bloodCellList.remove(bloodCells)

    # Move and Draw Bullets
    for bullets in bulletList:
        bullets.move()
        DS.blit(laserImage, (bullets.x, bullets.y))
        #if bullets.collisions(rect):
        #    score += 10
        #if not bullets.active:
        #    bulletList.remove(bullets)

    # Collisions Bullets and BloodCells
    for bloodCells in bloodCellList:
        if bloodCells.x < -bloodCells.width or not bloodCells.active:
            bloodCellList.remove(bloodCells)

        for bullets in bulletList:
            if not bullets.active:
                bulletList.remove(bullets)
            rect = bloodcellImage.get_rect(center=(bloodCells.x,bloodCells.y))

            if bullets.collisions(rect):
                score += 10
                bloodCells.active=False

    # Player
    player1.move()
    DS.blit(playerImage, (player1.x, player1.y))

    # Text
    # DS.blit(text, (width / 2 - text.get_width() // 2, 20 - text.get_height() // 2))
    drawText(DS, "Score: " + str(score), 24, width / 2, 5)
    drawText(DS, "Level: 1", 24, 50, 5)


# Game loop
while True:
    events()
    input()
    spawnBloodCells()
    move()

    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)
