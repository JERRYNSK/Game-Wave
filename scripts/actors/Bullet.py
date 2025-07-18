import pygame 
import math
class Bullet(pygame.sprite.Sprite):
    #nao eh uma bala, agora vai ser arrow, mas blz
    #posicoes da bala e do inimigo
    x = 0
    y = 0
    xdir = 0
    ydir = 0
    directon = None
    speed = 700

    def __init__(self, player, enemy):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.img.convert_alpha(), (25, 25))
        self.rect = self.image.get_rect()
        self.x = player.get_pos()[0]
        self.y = player.get_pos()[1] 
        self.rect.center = (self.x, self.y)
        if enemy != None:
            self.xdir = enemy.get_pos()[0]
            self.ydir = enemy.get_pos()[1]
        self.direction = pygame.Vector2(self.xdir - self.x, self.ydir - self.y).normalize()
        self.rotate()

    def update_game(self, player, enemy, dt):
        self.move(player, dt)
        
    
    def rotate(self):
        angle = math.degrees(math.atan2(-self.direction.y, self.direction.x)) - 45
        scaled_img = pygame.transform.scale(self.img, (64, 64))
        rotated_img = pygame.transform.rotate(scaled_img, angle)
        self.image = pygame.transform.scale(rotated_img, (32, 32))
        self.rect = self.image.get_rect(center=self.rect.center)
        #print(angle)
        
    def move(self, dt):

        self.x += self.direction.x * self.speed * dt
        self.y += self.direction.y * self.speed * dt
        self.rect.center = (self.x, self.y)



    