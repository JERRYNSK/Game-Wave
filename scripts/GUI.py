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
        text_number_wave = self.font.render('wave ' + str(wave.number_wave), False, (255, 255, 255))
        text_life = self.font.render(str(int(player.life)) + '/' + str(player.max_life), False, (200, 200, 200))
        screen.blit(text_number_wave, (400 - self.size_font/2, 25))
        screen.blit(text_life, (35, 20))

    #private
    def draw(self, screen, wave, player):
        pygame.draw.rect(screen, 'white', self.bar_max, 1)
        pygame.draw.rect(screen, 'white', self.bar_life)
        self.draw_grammar(screen, wave, player)
class Menu_game():
    #to com preguicsa de criar uma classe de botao
    button_play = None
    rect_play = None
    background = None
    def __init__(self):
        pygame.font.init()
        self.button_play = pygame.image.load('assets/buttons/btn_play.png')
        self.rect_play = self.button_play.get_rect()
        self.background = pygame.image.load('assets/bg_menu.png')



        

    def play(self, event):
        if self.is_mouse_in_area(self.rect_play) and event.type == pygame.MOUSEBUTTONDOWN:
            return True
        return False

    def is_mouse_in_area(self, rect):
        xm = pygame.mouse.get_pos()[0]
        ym = pygame.mouse.get_pos()[1]
        if xm > rect.x and xm < rect.x + rect.width and ym > rect.y and ym < rect.y + rect.height:
            return True
        return False



    def update(self, screen):
        self.draw(screen)

    def draw(self, screen):
        #por algum motivo o x e y do rect nao atualizam ent vou fazer no braço sapoxa
        x_position_play = 200
        y_position_play = 300
        self.rect_play.x = x_position_play
        self.rect_play.y = y_position_play
        screen.blit(self.background, (0,0))
        screen.blit(self.button_play, (x_position_play, y_position_play))

class Menu_lose():
    btn_reset = None
    reset_rect = None
    bg_lose = None
    def __init__(self):
        self.btn_reset = pygame.image.load('assets/buttons/btn_reset.png')
        self.bg_lose = pygame.image.load('assets/bg_lose.png')
        self.reset_rect = self.btn_reset.get_rect()
        self.reset_rect.x = 300
        self.reset_rect.y = 550

    def update(self, screen):
        screen.blit(self.bg_lose, (0,0))
        screen.blit(self.btn_reset, (300, 550))

    def reset_touched(self, event):
        if self.is_mouse_in_area(self.reset_rect) and event.type == pygame.MOUSEBUTTONDOWN:
            return True
        return False

    def is_mouse_in_area(self, rect):
        xm = pygame.mouse.get_pos()[0]
        ym = pygame.mouse.get_pos()[1]
        if xm > rect.x and xm < rect.x + rect.width and ym > rect.y and ym < rect.y + rect.height:
            return True
        return False
class Menu_win():
    bg_win = None
    def __init__(self):
        self.bg_win = pygame.image.load('assets/bg_win.png')
    
    def update(self, screen):
        screen.blit(self.bg_win, (0,0))

