import pygame
from pygame.locals import *
import Menu
from Player import *
from Laser import *
from Asteroid import *
import random
from GameOver import *
from Menu import *
import sys

pygame.init()
background_image = pygame.image.load("assets/background.jpg")
background = pygame.transform.scale(background_image, (800, 600))
pygame.display.set_caption('Asteroids-NEW HOPE')
screen = pygame.display.set_mode((800, 600))


def play_game():
    run = True
    timer = pygame.time.Clock()
    player = Player()
    playerlaser = []
    asteroids = []
    count = 0
    points = 0
    lives = 10
    font = pygame.font.Font('freesansbold.ttf', 18)
    while run:
        print(lives)
        print(points)
        timer.tick(60)
        count += 1
        if count % 50 == 0:
            run = random.choice([1, 1, 2])
            asteroids.append(Asteroid(run))
        for b in playerlaser:
            b.move()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(1)
        if keys[pygame.K_RIGHT]:
            player.move(2)
        if keys[pygame.K_UP]:
            player.boost()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playerlaser.append(Laser(player))
        if lives == 0:
            game_over(points)
        else:
            player.outofscreen()
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 30))
            for a in asteroids:
                screen.blit(a.asteroid, (a.x, a.y))
                a.x += a.xv
                a.y += a.yv
                if (a.x <= player.px <= a.x + a.w) or \
                        (a.x + a.w <= player.px + player.width // 2 and a.x
                         + a.w >= player.px - player.width // 2):
                    if (player.py - player.height // 2 <= a.y <= player.py
                        + player.height // 2) or \
                            (player.py - player.height // 2
                             <= a.y + a.h <= player.py + player.height // 2):
                        lives -= 1
                        asteroids.pop(asteroids.index(a))

                for b in playerlaser:
                    pygame.draw.rect(screen,
                                     (255, 0, 0), [b.x, b.y, b.w, b.h])
                    if (a.x <= b.x <= a.x + a.w) or \
                            (a.x <= b.x + b.w <= a.x + a.w):
                        if (a.y <= b.y <= a.y + a.h)\
                                or (a.y <= b.y + b.h <= a.y + a.h):
                            if a.level == 1:
                                points += 50
                                new_a1 = Asteroid(2)
                                new_a2 = Asteroid(2)
                                new_a1.x, new_a1.y = a.x, a.y
                                new_a2.x, new_a2.y = a.x, a.y
                                asteroids.append(new_a1)
                                asteroids.append(new_a2)
                            else:
                                points += 10
                            asteroids.pop(asteroids.index(a))
                            playerlaser.pop(playerlaser.index(b))
            life_bar = pygame.draw.rect(screen,
                                        (255, 0, 0), (20, 15, lives*10, 10))
            screen.blit(player.rotation, player.rotate_rect)
            score_font = font.render('Score: %s' % points, True,
                                     (255, 255, 255))
            score_rect = score_font.get_rect()
            score_rect.topleft = (650, 10)
            screen.blit(score_font, score_rect)
        pygame.display.flip()
    pygame.quit()
    pygame.display.update()
    sys.exit()


if __name__ == '__main__':
    Menu.access_menu()
