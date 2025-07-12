import pygame 
import random
class Power(pygame.sprite.Sprite):
    my_type = ''
    font = None
    screen = None
    player = None
    def __init__(self, path_img, type_power, position, player, scale):#position vai ser uma tupla fds
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.font = pygame.font.SysFont('assets/font/Minecraft.ttf', 50)
        self.my_type = type_power
        image = pygame.image.load(path_img)
        self.image = pygame.transform.scale(image, (scale, scale))
        self.rect = self.image.get_rect()
        self.rect.center = (position[0], position[1])
        self.player = player



    
    def update(self, screen, candraw):
        if candraw:
            screen.blit(self.image, self.rect)
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
            case 'max_life': self.player.max_life += random.choice((50,100))
            case 'cure': self.player.cure(50)
            case 'damage': self.player.damage_fire += 50
            case 'velocity_move': self.player.speed += 15
            case 'velocity_attack': self.player.set_fire_rate()
            


    def is_mouse_in_area(self):
        xm, ym = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        if xm > self.rect.x and xm < self.rect.x + self.rect.width and ym > self.rect.y and ym < self.rect.y + self.rect.height:
            return True
        return False
    def set_position(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def get_pos(self):
        return self.rect