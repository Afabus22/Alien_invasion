import sys
import pygame
from settings import Settings
from starship import Starship
from asteroid import Asteroid
import game_functions as gf


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    # Создание корабля.
    star_Destroyer = Starship(screen=screen)
    as1 = Asteroid(screen=screen)
    while True:
        gf.check_events(star_Destroyer)
        star_Destroyer.blitme()
        as1.blitme()
        pygame.display.flip()
        # При каждом проходе цикла перерисовывается экран.
        screen.fill(settings.bg_color)


run_game()
