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
        #colisoes entre inimigos
        
        

    def update_time(self):
        pass



    def nearest_enemy(self, player):

        self.minor = min(self.distance_list)
        for i in range(len(self.enemies_list)):
            self.distance_list[i] = self.enemies_list[i].distance
        for i in range(len(self.enemies_list)):
            if abs(self.minor - self.enemies_list[i].distance) < 1:
                return self.enemies_list[i]

        return self.enemies_list[0]

    def get_group(self):
        return self.enemy_group