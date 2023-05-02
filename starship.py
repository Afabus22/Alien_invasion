import pygame

class Starship():
    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('images/starship.png'), (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)