#imports of that shit
import pygame
from Wave import Wave
from actors.Player import Player
#init of game
pygame.init()
#variables
delta_time = 0
width_screen = 800
height_screen = 600
screen = pygame.display.set_mode((width_screen, height_screen))
player = Player()
wave_config = Wave()

clock_obj = pygame.time.Clock()
#group to actors
player_group_sprite = pygame.sprite.Group()
enemy_group_sprite = pygame.sprite.Group()
bullet_group_sprite = pygame.sprite.Group()

player_group_sprite.add(player)


#functions of game to paiagame 
def update_game():
    global delta_time
    #wave config
    player.update_game(screen, wave_config.nearest_enemy(player), wave_config.there_enemy(), delta_time)
    wave_config.update(screen, player, delta_time)
    #updating group
    player_group_sprite.update(screen)
    actualize_groups_sprites()
    #handle inputs
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
    delta_time = clock_obj.tick(60) / 1000
    #print(delta_time)

def draw_game():
    screen.fill((0, 0, 0))
    #drawing group
    player_group_sprite.draw(screen)

def actualize_groups_sprites():
    #usaremos mais tarde quando quiusermos colidir player e inimigp(xp) e balas tmb
    enemy_group_sprite = wave_config.get_group()
    bullet_group_sprite = player.get_bullets_sprite_group()
    #collisions handle
    colisions = pygame.sprite.groupcollide(enemy_group_sprite, bullet_group_sprite, True, True)


#loop of the paiagame
while(True):
    draw_game()
    update_game()
    #final
    clock_obj.tick(60)
    pygame.display.update()
    
    #GOSTARIA DE AGRADECER À PROFESSORA SENHORA RENATA, POIS DEVIDO A ELA CONSEGUI FAZER DE FORMA AUTÔNOMA A PARTE MATEMÀTICA DO JOGOOOOOOOOOOO ainnnnnnnnnnn
