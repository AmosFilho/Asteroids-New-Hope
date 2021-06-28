
class Laser:
    def __init__(self, player):
        self.point = player.front
        (self.x, self.y) = self.point
        self.w = 4
        self.h = 4
        self.c = player.directionx
        self.s = player.directiony
        self.xv = self.c * 13
        self.yv = self.s * 13

    def move(self):
        self.x += self.xv
        self.y -= self.yv
