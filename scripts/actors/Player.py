import pygame
from actors.Bullet import Bullet

class Player(pygame.sprite.Sprite):
    #variables
    range_fire = 200
    damage_fire = 50
    x_position = 400
    y_position = 300
    velocity_x = 0
    velocity_y = 0
    speed = 500
    cooldown_fire_timer = 0
    timer_to_fire = 0.1
    bullets_list = []
    bullet_group = pygame.sprite.Group()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.img.convert_alpha(), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)  # initial position ;-;
    


    def move(self, dt):
        global x_position
        global y_position
        global velocity_x
        global velocity_y

        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_w]:
            self.velocity_y = - 1
        elif self.keys[pygame.K_s]:
            self.velocity_y = 1
        else:
            self.velocity_y = 0
        if self.keys[pygame.K_d]:
            self.velocity_x = 1
        elif self.keys[pygame.K_a]:
            self.velocity_x = -1
        else:
            self.velocity_x = 0
        
        #normalization 
        if self.velocity_x != 0 or self.velocity_y != 0:
            self.normalized_move = pygame.Vector2(self.velocity_x, self.velocity_y).normalize()
            self.x_position += self.normalized_move.x * self.speed * dt
            self.y_position += self.normalized_move.y * self.speed * dt

        self.rect.center = (self.x_position, self.y_position)#actualize the position
    def update_game(self, screen,enemy, canshoot, dt):
        self.move(dt)
        if canshoot:
            self.fire(enemy, dt)
        self.bullet_group.draw(screen)
    def get_pos(self):
        return self.x_position, self.y_position

    def fire(self, enemy, dt):
        if enemy.distance < self.range_fire and self.cooldown_fire_timer > self.timer_to_fire:
            self.bullet = Bullet(self, enemy)
            self.bullets_list.append(self.bullet)
            self.bullet_group.add(self.bullet)
            self.cooldown_fire_timer = 0
        else:
            self.cooldown_fire_timer += 0.01
        if self.bullets_list:
            for i in self.bullets_list:
                i.move(self, dt)



    def get_bullets_sprite_group(self):
        return self.bullet_group




        
#nao faço ideia de como colocar sistema de cartas aq

#im not throw away my shot:0