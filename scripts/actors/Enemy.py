import pygame

class Enemy(pygame.sprite.Sprite):
    #variables 
    life = 100
    timer_to_attack = 0
    x_position = 100
    y_position = 100
    velocity_x = 0
    velocity_y = 0
    distance = 0
    speed = 150
    damage = 10
    #sound
    sound_die = None
    #tipo de inimigo vao ser tres: os normais, os explosivos e atiradores
    type_enemy = None
    def __init__(self, pos, typeof = 'normal'):
        pygame.sprite.Sprite.__init__(self)
        pygame.mixer.init()
        type_enemy = typeof
        self.img = pygame.image.load('assets/enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.img.convert_alpha(), (120, 100))
        self.rect = self.image.get_rect()
        
        self.x_position = pos[0]
        self.y_position = pos[1]    
        self.rect.center = (self.x_position, self.y_position)  # initial position:)
        self.sound_die = pygame.mixer.Sound('assets/sounds/hurt.wav')

    
    def update_game(self, player, dt):
       self.move(player, dt)


    def move(self, player, dt):
        self.direction = pygame.Vector2(player.get_pos()[0] - self.x_position, player.get_pos()[1] - self.y_position)
        self.distance = self.direction.length()
        if self.distance > 50:#is afastado
            self.x_position += self.direction.normalize().x * self.speed * dt
            self.y_position += self.direction.normalize().y * self.speed * dt
            timer_to_attack = 0
        else: #isnt afastado
            self.timer_to_attack += dt
            if self.timer_to_attack > 0.1:
                player.set_life(self.damage)
                self.timer_to_attack = 0
        self.rect.center = (self.x_position, self.y_position)

    def set_life(self, value):
        self.life -= value
        if self.life <= 0.0:
            self.sound_die.play()
            self.kill()
    #function that revive and set new atribuitions to enemy like life, speed...
    def reset(self, parameter_skill):
        self.life = 100 + parameter_skill * 100
        self.speed = 250 + parameter_skill * self.speed/2
        self.damage = 10 + parameter_skill * self.damage
    def set_position(self, pos):
        self.x_position = pos[0]
        self.y_position = pos[1]
        self.rect.center = (self.x_position, self.y_position)
    def get_pos(self):
        return self.x_position, self.y_position
