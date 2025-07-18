import pygame 
import random
class Power(pygame.sprite.Sprite):
    my_type = ''
    font = None
    screen = None
    player = None
    is_max = False
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
        if candraw and not self.is_max:
            screen.blit(self.image, self.rect)
        self.screen = screen
        if self.is_mouse_in_area() and candraw and not self.is_max:
            pygame.draw.rect(self.screen, 'white', self.rect, 3)
        self.update_max()



        
    def update_max(self):
        #se a ahabilidade está maximixaa, desativa a carta
        #max life, cure, serao inifinitos
        match self.my_type:
            case 'range': 
                self.is_max = self.player.range_fire > 600
            case 'damage': 
                self.is_max = self.player.damage_fire >= 200 
            case 'velocity_move': 
                self.is_max = self.player.speed > 1000
            case 'velocity_attack': 
                self.is_max = self.player.timer_to_fire <= 0.01


    def touched_power(self, input, can_give_power):
        if self.is_mouse_in_area() and input.type == pygame.MOUSEBUTTONDOWN and can_give_power and not self.is_max:
            self.give_power(self.my_type)
            return True
        return False

    def give_power(self, type_power):
        #obrigado switch case  por existir te amoooo
        match type_power:
            case 'range': 
                self.player.range_fire += 50
                print('range')
            case 'max_life': 
                self.player.max_life += random.choice((50,100))
                print('max vida')
            case 'cure': 
                self.player.cure(50)
                print('cura')
            case 'damage': 
                self.player.damage_fire += 50
                print('dano')
            case 'velocity_move': 
                self.player.speed += 50
                print('movimento rapido')
            case 'velocity_attack': 
                self.player.set_fire_rate()
                print('ataque rapido')
            


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

    def reset(self):
        self.is_max = False