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
#usaremos mais tarde quando quiusermos colidir player e inimigp(xp) e balas tmb
enemy_group_sprite = wave_config.get_group()

#functions of game to paiagame 
def update_game():
    global delta_time
    #actualize deltatime
    delta_time = clock_obj.tick(60) / 1000
    #wave config
    player.update_game(screen, wave_config.nearest_enemy(player), delta_time)
    wave_config.update(screen, player, delta_time)
    #updating group
    player_group_sprite.update(screen)
    #handle inputs
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()

def draw_game():
    screen.fill((0, 0, 0))
    #drawing group
    player_group_sprite.draw(screen)


#loop of the paiagame
while(True):
    draw_game()
    update_game()
    #final
    pygame.display.update()
    clock_obj.tick(60)