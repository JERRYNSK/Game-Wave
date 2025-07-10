import pygame

class Enemy(pygame.sprite.Sprite):
    #variables 
    life = 100
    x_position = 100
    y_position = 100
    velocity_x = 0
    velocity_y = 0
    distance = 0
    speed = 250
    damage = 10
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.img.convert_alpha(), (120, 100))
        self.rect = self.image.get_rect()

        self.x_position = pos[0]
        self.y_position = pos[1]    
        self.rect.center = (self.x_position, self.y_position)  # initial position:)

    
    def update_game(self, player, dt):
       self.move(player, dt)


    def move(self, player, dt):
        self.direction = pygame.Vector2(player.get_pos()[0] - self.x_position, player.get_pos()[1] - self.y_position)
        self.distance = self.direction.length()
        if self.distance > 10:
            self.x_position += self.direction.normalize().x * self.speed * dt
            self.y_position += self.direction.normalize().y * self.speed * dt
        self.rect.center = (self.x_position, self.y_position)


    def set_position(self, pos):
        self.x_position = pos[0]
        self.y_position = pos[1]
        self.rect.center = (self.x_position, self.y_position)
    def get_pos(self):
        return self.x_position, self.y_position
