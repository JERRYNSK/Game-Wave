import pygame
from actors.Enemy import Enemy 
import math
import random
class Wave():
    #vou usar pooling pra evitar o crash
    #variables
    can_spawn = False
    number_wave = 1
    
    max_enemies = 1
    timer = 0
    enemies_list = []
    dead_enemies_list = []
    distance_list = []
    enemy_group = pygame.sprite.Group()
    increase = 0.01#thinks its percent
    
    

    def __init__(self):
        self.instance_enemies()

           
    def instance_enemies(self, bool = False):
        for i in range(self.max_enemies):
            if bool:
                self.enemies_list.append(Enemy(self.random_position()))
                self.distance_list.append(0)
            else:
                self.enemies_list.append(Enemy(self.random_position(), 'explosive'))
                self.distance_list.append(0)
        for i in self.enemies_list:
            self.enemy_group.add(i)

    def spawn_enemies(self, screen):
        index = 0
        for i in self.dead_enemies_list:
            self.enemies_list.append(i)
            self.distance_list.append(0)
            i.set_position(self.random_position())
            self.enemy_group.add(i)
            self.enemy_group.update(screen)
            #recharge the life>:)
            i.reset(self.increase)
        self.dead_enemies_list = []
        self.number_wave += 1
        self.can_spawn = False

    def random_position(self):
        #coordenada x será o input
        rand_x = random.uniform(-1, 1) * 800 + 400
        a = 640000
        b = (rand_x) ** 2
        y_output = (abs((a - b)) ** 0.5) + 300
        return rand_x, y_output * random.choice((-1, 1))
#por algum motivo dá erro de invalid rect, pelo menos o codigo atual funciona realativamente bem:]
       

    def update(self, screen, player, dt):
        
        for i in self.enemies_list:
            i.update_game(player, dt)
        self.when_sprite_dead()
        #SE NAO HOUVER INIMIGOS, ELE DÁ SPANW, CUIDADO POHA
        if not self.there_enemy() and self.can_spawn:
            self.add_enemies()
            self.spawn_enemies(screen)
            #aumenta 
        #se tem inimigos poem eles de volta a acao
        if self.there_enemy():
            self.enemy_group.update(screen)
            self.enemy_group.draw(screen)
        

    def add_enemies(self):
        match self.number_wave:
            case 3: 
                self.max_enemies = 5
                self.instance_enemies(True)
                self.increase = 0.05
            case 20:
                self.max_enemies = 15
                self.instance_enemies()
                self.increase = 0.1
            case 30:
                self.max_enemies = 30
                self.instance_enemies()
                self.increase = 0.5
            case 40:
                self.max_enemies = 50
                self.instance_enemies()
            case 55:
                self.max_enemies = 50
                self.instance_enemies()
                self.increase = 1

    def set_can_spawn(self):
        self.can_spawn = True
        
    def when_sprite_dead(self):
        for i in self.enemies_list:
            if not i.alive():
                self.dead_enemies_list.append(i)
                self.enemies_list.remove(i)
                del self.distance_list[len(self.distance_list) - 1]



    



    def nearest_enemy(self, player):
        if self.there_enemy():
            for i in range(len(self.enemies_list)):
                self.distance_list[i] = self.enemies_list[i].distance
            for i in self.enemies_list:
                self.minor = min(self.distance_list)
                if math.isclose(self.minor, i.distance):
                    return i
                

        return None
    def there_enemy(self):
        return len(self.enemies_list) != 0

    def get_group(self):
        return self.enemy_group

    #tem q resetar
    def reset(self):
        self.can_spawn = False
        self.number_wave = 1
    
        self.max_enemies = 1
        self.timer = 0
        self.enemies_list = []
        self.dead_enemies_list = []
        self.distance_list = []
        self.increase = 0.01#thinks its percent
        self.enemy_group.empty()
        self.instance_enemies()
    
        

#stackoverflow paga nois