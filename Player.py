import pygame
import math

pygame.init()
background_image = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background_image, (800, 600))
pygame.display.set_caption('Asteroids-NEW HOPE')
screen = pygame.display.set_mode((800, 600))


class Player:
    player_image = pygame.image.load("assets/MillenniumFalcon.png")
    player = pygame.transform.scale(player_image, (50, 50))

    def __init__(self):
        self.px = 400
        self.py = 300
        self.width = self.player.get_width()
        self.height = self.player.get_height()
        self.angle = 0
        self.rotation = pygame.transform.rotate(self.player, self.angle)
        self.rotate_rect = self.rotation.get_rect()
        self.rotate_rect.center = (self.px, self.py)
        self.directionx = math.cos(math.radians(self.angle + 90))
        self.directiony = math.sin(math.radians(self.angle + 90))
        self.front = (self.px + self.directionx * self.width//2, self.py - self.directiony * self.height//2)

    def move(self, direction):
        if direction == 1:
            self.angle += 5
        elif direction == 2:
            self.angle -= 5
        self.rotation = pygame.transform.rotate(self.player, self.angle)
        self.rotate_rect = self.rotation.get_rect()
        self.rotate_rect.center = (self.px, self.py)
        self.directionx = math.cos(math.radians(self.angle + 90))
        self.directiony = math.sin(math.radians(self.angle + 90))
        self.front = (self.px + self.directionx * self.width//2, self.py - self.directiony * self.height//2)

    def boost(self):
        self.px += self.directionx * 6
        self.py -= self.directiony * 6
        self.rotation = pygame.transform.rotate(self.player, self.angle)
        self.rotate_rect = self.rotation.get_rect()
        self.rotate_rect.center = (self.px, self.py)
        self.directionx = math.cos(math.radians(self.angle + 90))
        self.directiony = math.sin(math.radians(self.angle + 90))
        self.front = (self.px + self.directionx * self.width//2, self.py - self.directiony * self.height//2)

    def outofscreen(self):
        if self.px > 850:
            self.px = 400
        elif self.px < -50:
            self.px = 400
        if self.py > 650:
            self.py = 300
        elif self.py < 30:
            self.py = 300
