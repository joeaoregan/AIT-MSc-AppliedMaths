x, y = 1280, 360
angle = 0


def move():
    global x, angle
    x -= 3

    if x < 0:
        x = 1280

    angle += 2
    angle %= 360
    # angle % 360
