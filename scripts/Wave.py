import pygame
from actors.Enemy import Enemy 
import math
import random
class Wave():
    #vou usar pooling pra evitar o crash
    #variables
    can_spawn = False
    max_enemies = 20
    timer = 0
    enemies_list = []
    dead_enemies_list = []
    distance_list = []
    enemy_group = pygame.sprite.Group()
    #locais de spawn
    locals_spawn = [(200, -100), (400, -100) , (600, -100) , (800, -100) , (0, 700)]
    
    

    def __init__(self):
        self.instance_enemies()

           
    def instance_enemies(self):
        for i in range(self.max_enemies):
            self.enemies_list.append(Enemy(self.random_position()))
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
        self.dead_enemies_list = []

    def random_position(self):
        #coordenada x será o input
        rand_x = random.random() * 800
        y_output = (abs( (640000 * (2) ** (1/2)) - (rand_x * rand_x))) ** (1/2) * random.choice((-1, 1))
        return rand_x, y_output



       

    def update(self, screen, player, dt):
        
        for i in self.enemies_list:
            i.update_game(player, dt)
        self.when_sprite_dead()
        #SE NAO HOUVER INIMIGOS, ELE DÁ SPANW, CUIDADO POHA
        if not self.there_enemy():
            self.spawn_enemies(screen)
        if self.there_enemy():
            self.enemy_group.update(screen)
            self.enemy_group.draw(screen)

        
        
    def when_sprite_dead(self):
        for i in self.enemies_list:
            if not i.alive():
                self.dead_enemies_list.append(i)
                self.enemies_list.remove(i)
                del self.distance_list[len(self.distance_list) - 1]



    def update_time(self):
        pass



    def nearest_enemy(self, player):
        if self.there_enemy():
            for i in range(len(self.enemies_list)):
                self.distance_list[i] = self.enemies_list[i].distance
            for i in self.enemies_list:
                self.minor = min(self.distance_list)
                if math.isclose(self.minor, i.distance):
                    print(i.distance)
                    return i
                

        return None
    def there_enemy(self):
        return len(self.enemies_list) != 0

    def get_group(self):
        return self.enemy_group