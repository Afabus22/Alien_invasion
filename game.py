import sys
import pygame
from settings import Settings
from starship import Starship
from asteroid import Asteroid

def run_game():
    # Инициализирует игру и создает объект экрана.
      pygame.init()
      settings = Settings()
      screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
      # Создание корабля.
      star_Destroyer = Starship(screen=screen)
      as1 = Asteroid(screen=screen)
      while True:
        for event in pygame.event.get(): # event - событие get - получать
          if event.type == pygame.QUIT: # type - тип, QUIT - выйти
              sys.exit()
        star_Destroyer.blitme()
        as1.blitme()
        pygame.display.flip()


run_game()