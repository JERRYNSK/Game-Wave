import pygame
class Barlife():
    x = 10
    y = 10
    bar_max = None#barra q vai denotar a vida max
    bar_life = None
    #grammar
    font = None
    size_font = 20
    def __init__(self):
        self.bar_max = pygame.Rect(self.x, self.y, 100, 30)
        self.bar_life = pygame.Rect(self.x, self.y, 90, 30)
        pygame.font.init()
        self.font = pygame.font.SysFont('assets/font/Minecraft.ttf', self.size_font)


    def update(self, screen, player, wave):
        self.bar_life = pygame.Rect(self.x, self.y, 100 * (player.life/player.max_life), 30)
        self.draw(screen, wave, player)
    
    def draw_grammar(self, screen, wave, player):
        text_number_wave = self.font.render('wave' + str(wave.number_wave), False, (255, 255, 255))
        text_life = self.font.render(str(int(player.life)) + '/' + str(player.max_life), False, (200, 200, 200))
        screen.blit(text_number_wave, (400 - self.size_font/2, 25))
        screen.blit(text_life, (35, 20))

    #private
    def draw(self, screen, wave, player):
        pygame.draw.rect(screen, 'white', self.bar_max, 1)
        pygame.draw.rect(screen, 'white', self.bar_life)
        self.draw_grammar(screen, wave, player)

