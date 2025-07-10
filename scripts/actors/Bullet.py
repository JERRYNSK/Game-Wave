import pygame 
class Bullet(pygame.sprite.Sprite):
    #nao eh uma bala, agora vai ser arrow, mas blz
    #posicoes da bala e do inimigo
    x = 0
    y = 0
    xdir = 0
    ydir = 0
    directon = None
    speed = 1500

    def __init__(self, player, enemy):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/bullet.png').convert_alpha()
        self.image = pygame.transform.scale(self.img.convert_alpha(), (50, 50))
        self.rect = self.image.get_rect()
        self.x = player.get_pos()[0]
        self.y = player.get_pos()[1] 
        self.rect.center = (self.x, self.y)
        if enemy != None:
            self.xdir = enemy.get_pos()[0]
            self.ydir = enemy.get_pos()[1]
        self.direction = pygame.Vector2(self.xdir - self.x, self.ydir - self.y).normalize()

    def update_game(self, player, enemy, dt):
        self.move(player, dt)
        
    def move(self, player, dt):

        self.x += self.direction.x * self.speed * dt
        self.y += self.direction.y * self.speed * dt
        self.rect.center = (self.x, self.y)



    