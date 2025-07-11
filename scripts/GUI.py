import pygame
class Barlife():
    x = 10
    y = 10
    bar_max = None#barra q vai denotar a vida max
    bar_life = None
    def __init__(self):
        self.bar_max = pygame.Rect(self.x, self.y, 100, 30)
        self.bar_life = pygame.Rect(self.x, self.y, 90, 30)


    def update(self, screen, player):
        self.bar_life = pygame.Rect(self.x, self.y, 100 * (player.life/player.max_life), 30)
        self.draw(screen)

    #private
    def draw(self, screen):
        pygame.draw.rect(screen, 'white', self.bar_max, 1)
        pygame.draw.rect(screen, 'white', self.bar_life)

