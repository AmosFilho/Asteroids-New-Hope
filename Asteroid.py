import pygame
import random


class Asteroid:
    def __init__(self, level):
        self.level = level
        if self.level == 1:
            self.image = pygame.image.load("assets/asteroid.png")
            self.asteroid = pygame.transform.scale(self.image, (60, 60))
        elif self.level == 2:
            self.image = pygame.image.load("assets/asteroidl.png")
            self.asteroid = pygame.transform.scale(self.image, (30, 30))
        self.w = 60/level
        self.h = 60/level
        self.score = 2
        self.spawn = random.choice([(random.randrange(0, 800 - self.w), random.choice([-1 * self.h - 5, 600 + 5])),
                                    (random.choice([-1 * self.w - 5, 800 + 5]), random.randrange(0, 600 - self.h))])
        self.x, self.y = self.spawn
        self.xdir, self.ydir = (0, 0)
        if self.x < 400:
            self.xdir = 1
        elif self.x > 400:
            self.xdir = -1
        if self.y < 300:
            self.ydir = 1
        elif 300 < self.y:
            self.ydir = -1
        self.xv = self.xdir * random.randrange(1, 3)
        self.yv = self.ydir * random.randrange(1, 3)
