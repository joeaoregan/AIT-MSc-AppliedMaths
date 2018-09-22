import AntiBody.object as object
# x, y = 1280, 360
# angle = 0

class BloodCell(object.Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = 0
        self.velocityY = 0
        self.angle = 0

    def move(self):
        # global x, angle
        self.x -= 3

        if self.x < 0:
            self.x = 1280

        self.angle += 2
        self.angle %= 360
