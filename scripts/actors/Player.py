import pygame
from actors.Bullet import Bullet
class Player(pygame.sprite.Sprite):
    #variables
    max_life = 100
    life = 20
    range_fire = 200
    damage_fire = 50
    x_position = 400
    y_position = 300
    velocity_x = 0
    velocity_y = 0
    speed = 300
    cooldown_fire_timer = 0
    timer_to_fire = 0.5
    bullets_list = []
    bullet_group = pygame.sprite.Group()
    #variabls to animation
    timer_to_frame = 0
    index_frame = 0
    list_sprite_animation = []
    dead_sprite = None
    #sound
    sound_fire = None



    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.mixer.init()
        self.img = pygame.image.load('assets/player.png').convert_alpha()
        self.dead_sprite = pygame.image.load('assets/player_animation/player_dead.png').convert_alpha()
        self.image = pygame.transform.scale(self.img.convert_alpha(), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)  # initial position ;-;
        self.sound_fire = pygame.mixer.Sound('assets/sounds/shot.wav')
        self.load_frames()
    
    def load_frames(self):
        a = pygame.image.load('assets/player_animation/idle.png').convert_alpha()
        b = pygame.image.load('assets/player_animation/walk0.png').convert_alpha()
        c = pygame.image.load('assets/player_animation/walk1.png').convert_alpha()
        d = pygame.image.load('assets/player_animation/walk2.png').convert_alpha()
        e = pygame.image.load('assets/player_animation/walk3.png').convert_alpha()

        self.list_sprite_animation.append(a)
        self.list_sprite_animation.append(b)
        self.list_sprite_animation.append(c)
        self.list_sprite_animation.append(d)
        self.list_sprite_animation.append(e)

    def animate(self, dt):
        if (self.velocity_x != 0 or self.velocity_y != 0) and self.is_alive():
            self.timer_to_frame += dt
            if self.timer_to_frame > 0.1:
                self.index_frame += 1
                if self.index_frame >= len(self.list_sprite_animation):
                    self.index_frame = 0
                self.image = pygame.transform.scale(self.list_sprite_animation[self.index_frame], (75, 75))
                self.timer_to_frame = 0
        elif self.is_alive(): 
            self.image =pygame.transform.scale(self.list_sprite_animation[0], (75, 75))
        else:
            self.image = pygame.transform.scale(self.dead_sprite, (75, 75))





    def move(self, dt):
        
        self.keys = pygame.key.get_pressed()
        
        if self.keys[pygame.K_w] or self.keys[pygame.K_UP]:
            self.velocity_y = - 1
        elif self.keys[pygame.K_s]or self.keys[pygame.K_DOWN]:
            self.velocity_y = 1
        else:
            self.velocity_y = 0
        if self.keys[pygame.K_d] or self.keys[pygame.K_RIGHT]:
            self.velocity_x = 1
        elif self.keys[pygame.K_a] or self.keys[pygame.K_LEFT]:
            self.velocity_x = -1
        else:
            self.velocity_x = 0
        
        #normalization 
        if self.velocity_x != 0 or self.velocity_y != 0:
            self.normalized_move = pygame.Vector2(self.velocity_x, self.velocity_y).normalize()
            self.x_position += self.normalized_move.x * self.speed * dt
            self.y_position += self.normalized_move.y * self.speed * dt
        #NAO PODE PASSAR DAS BARREIRAS
        scale_player = 75/2
        if self.x_position < scale_player:
            self.x_position = scale_player
        elif self.x_position > 800 - scale_player:
            self.x_position = 800 - scale_player
        if self.y_position < scale_player:
            self.y_position = scale_player
        elif self.y_position > 600 - scale_player:
            self.y_position = 600 - scale_player
        self.rect.center = (self.x_position, self.y_position)#actualize the position


    def update_game(self, screen,enemy, canshoot, dt):
        if self.is_alive():
            self.move(dt)
            if canshoot:
                self.fire(enemy, dt)
            self.bullet_group.draw(screen)
        self.animate(dt)
        

    def get_pos(self):
        return self.x_position, self.y_position

    def fire(self, enemy, dt):
        if enemy.distance < self.range_fire and self.cooldown_fire_timer > self.timer_to_fire:
            self.bullet = Bullet(self, enemy)
            self.bullets_list.append(self.bullet)
            self.bullet_group.add(self.bullet)
            self.sound_fire.play()
            self.cooldown_fire_timer = 0
        else:
            self.cooldown_fire_timer += 0.01
        if self.bullets_list:
            for i in self.bullets_list:
                i.move(dt)


    def set_life(self, damage):
        if self.life >= 0:
            self.life -= damage
    def cure(self, value):
        if self.life + value < self.max_life:
            self.life += value
        else:
            self.life = self.max_life
    def set_fire_rate(self):
        if self.timer_to_fire > 0.01:
            self.timer_to_fire -= 0.05
    def is_alive(self):
        return self.life >= 0
    def get_bullets_sprite_group(self):
        return self.bullet_group
    
    #quando o jogo acabar tem q resetar
    def reset(self):
        self.max_life = 100
        self.life = 100
        self.range_fire = 200
        self.damage_fire = 50
        self.x_position = 400
        self.y_position = 300
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 300
        self.cooldown_fire_timer = 0
        self.timer_to_fire = 0.5

        self.timer_to_frame = 0
        self.index_frame = 0
        




        
#nao faço ideia de como colocar sistema de cartas aq

#im not throw away my shot:0