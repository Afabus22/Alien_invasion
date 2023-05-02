import pygame

class Asteroid():
    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images/asteroid.png'), (100, 150))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)