import pygame
from main import *
import main
import sys

pygame.init()
window = pygame.display.set_mode((800, 600))
window_rect = window.get_rect()
pygame.display.set_caption('Asteroids-NEW HOPE')


# Menu Function
def access_menu():
    touch = True
    while touch:
        window.fill((0, 0, 0))
        # Menu templates
        title_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
        menu_text = title_font.render('Asteroids', True, (255, 255, 255))
        menu_text_rect = menu_text.get_rect()
        menu_text_rect.center = (392, 100)
        subtitle_font = pygame.font.Font(
            'assets/PressStart2P.ttf', 10)
        credit = subtitle_font.render('@Based on Star Wars series',
                                      True, (255, 255, 255))
        subtitle_text = title_font.render('NEW HOPE', True, (255, 255, 0))
        subtitle_text_rect = subtitle_text.get_rect()
        subtitle_text_rect.center = (392, 140)
        play_font = pygame.font.Font('assets/PressStart2P.ttf', 20)
        text_1 = 'PLAY'
        text_3 = 'EXIT'
        text_1 = play_font.render(text_1, True, (255, 255, 255))
        text_3 = play_font.render(text_3, True, (255, 255, 255))
        text_1_rect = text_1.get_rect()
        text_3_rect = text_3.get_rect()
        text_1_rect.center = (392, 234)
        text_3_rect.center = (392, 264)
        # Get the mouse position and verifies collision with buttons
        pos_mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_1_rect.collidepoint(pos_mouse):
                    main.play_game()
                    touch = False
                if text_3_rect.collidepoint(pos_mouse):
                    pygame.quit()
                    sys.exit()
            # Spawn objects on screen
            window.blit(credit, (10, 550))
            window.blit(menu_text, menu_text_rect)
            window.blit(subtitle_text, subtitle_text_rect)
            window.blit(text_1, text_1_rect)
            window.blit(text_3, text_3_rect)
            pygame.display.update()


if __name__ == '__main__':
    access_menu()
