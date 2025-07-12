import pygame 
class Power(pygame.sprite.Sprite):
    my_type = ''
    text_type = ''
    font = None
    screen = None
    player = None
    def __init__(self, path_img, type_power, position, player):#position vai ser uma tupla fds
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.font = pygame.font.SysFont('assets/font/Minecraft.ttf', 15)
        self.my_type = type_power
        self.image = pygame.image.load(path_img)
        self.rect = self.image.get_rect()
        self.rect.center = (position[0], position[1])
        self.player = player
        self.set_text_type()

    def set_text_type(self):
        match self.my_type:
            case 'range': self.text_type = 'Maior distância de ataque'



    
    def update(self, screen, candraw):
        if candraw:
            screen.blit(self.image, self.rect)
            self.draw_text(screen)
        self.screen = screen
        if self.is_mouse_in_area() and candraw:
            pygame.draw.rect(self.screen, 'white', self.rect, 1)


    def touched_power(self, input):
        if self.is_mouse_in_area() and input.type == pygame.MOUSEBUTTONDOWN:
            self.give_power(self.my_type)
            return True
        return False

    def give_power(self, type_power):
        #obrigado switch case  por existir te amoooo
        match type_power:
            case 'range': self.player.range_fire += 50
            case 'max_life': self.player.max_life += 10


    def draw_text(self, screen):
        text = self.font.render(self.text_type, False, (255,255,255))
        screen.blit(text, (self.rect.x , self.rect.y + 20))

    def is_mouse_in_area(self):
        xm, ym = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        if xm > self.rect.x and xm < self.rect.x + self.rect.width and ym > self.rect.y and ym < self.rect.y + self.rect.height:
            return True
        return False
