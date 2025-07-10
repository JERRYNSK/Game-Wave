import pygame
from actors.Enemy import Enemy 
import math
class Wave():
    #variables
    can_spawn = False
    max_enemies = 5
    timer = 0
    enemies_list = []
    distance_list = []
    enemy_group = pygame.sprite.Group()
    
    

    def __init__(self):
        self.spawn_enemies()
           
    def spawn_enemies(self):
        offset = 0
        for i in range(self.max_enemies):
            self.enemies_list.append(Enemy(300, offset))
            self.distance_list.append(0)
            offset += 150
        for i in self.enemies_list:
            self.enemy_group.add(i)
       

    def update(self, screen, player, dt):
        self.enemy_group.update(screen)
        self.enemy_group.draw(screen)
        for i in self.enemies_list:
            i.update_game(player, dt)
        self.when_sprite_dead()
        #SE NAO HOUVER INIMIGOS, ELE DÁ SPANW, CUIDADO POHA
        if not self.there_enemy():
            self.spawn_enemies()

        
        
    def when_sprite_dead(self):
        for i in self.enemies_list:
            if not i.alive():
                self.enemies_list.remove(i)
                del self.distance_list[len(self.distance_list) - 1]



    def update_time(self):
        pass



    def nearest_enemy(self, player):
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