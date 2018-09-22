import pygame


def rotate(image, rect, angle):
    """Rotate the image while keeping its center."""
    # Rotate the original image without modifying it.
    new_image = pygame.transform.rotate(image, angle)
    # Get a new rect with the center of the old rect.
    rect = new_image.get_rect(center=rect.center)
    return new_image, rect


def main():
    clock = pygame.time.Clock()
    DS = pygame.display.set_mode((640, 480))
    gray = pygame.Color('gray15')
    # blue = pygame.Color('dodgerblue2')

    bloodcellImage = pygame.image.load("BloodCell.png").convert()
    # image = pygame.Surface((320, 200), pygame.SRCALPHA)
    #pygame.draw.polygon(image, blue, ((0, 0), (320, 100), (0, 200)))
    # Keep a reference to the original to preserve the image quality.
    orig_image = bloodcellImage
    x = 320
    angle = 0

    done = False

    while not done:
        rect = bloodcellImage.get_rect(center=(x, 240))
        x-=3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        angle += 2
        bloodcellImage, rect = rotate(orig_image, rect, angle)

        DS.fill(gray)
        DS.blit(bloodcellImage, rect)
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
