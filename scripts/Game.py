#imports of that shit
import pygame
from Wave import Wave
from GUI import Barlife
from actors.Player import Player
from Powers import Power
#init of game
pygame.init()
#variables
delta_time = 0
width_screen = 800
height_screen = 600
screen = pygame.display.set_mode((width_screen, height_screen))
background = pygame.image.load('assets/background.png')
player = Player()
wave_config = Wave()
barlife = Barlife()

clock_obj = pygame.time.Clock()
#lista para as cartas, o player vai poder escolher um a cada wave, sem poha de re rol
#tipos: range, max_life, cure, damage, velocity_move, velocity_attack
scale_card = 250
offset = 10
offset_card = scale_card + offset#pixseis
#cada carta eh 100x100 pixeis
fixed_x = 135
fixed_y = 450
cards_list = []
cards_list.append(Power('assets/cards/card_attack_range.png', 'range', (fixed_x,fixed_y - offset_card), player, scale_card))
cards_list.append(Power('assets/cards/card_max_life.png', 'max_life', (200,fixed_y - offset_card), player, scale_card))
cards_list.append(Power('assets/cards/card_cure.png', 'cure', (200, fixed_y - offset_card), player, scale_card))
cards_list.append(Power('assets/cards/card_damage.png', 'damage', (fixed_x,fixed_y), player, scale_card))
cards_list.append(Power('assets/cards/card_velocity_move.png', 'velocity_move', (200,fixed_y), player, scale_card))
cards_list.append(Power('assets/cards/card_velocity_attack.png', 'velocity_attack', (200,fixed_y), player, scale_card))
#for para organizar
matriz_organize = [
    [cards_list[0], cards_list[1], cards_list[2]],
    [cards_list[3], cards_list[4], cards_list[5]]
]

for i in range(2):  # linhas da matriz
    for j in range(1, 3):  # colunas a partir do segundo item (índice 1 e 2)
        anterior = matriz_organize[i][j - 1]
        atual = matriz_organize[i][j]

        x_card = anterior.get_pos()[0] + offset_card
        y_card = anterior.get_pos()[1]  # ou matriz_organize[i][0] se preferir

        atual.set_position((x_card, y_card))


    


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


    #cartas
    for cards in cards_list:
        cards.update(screen, not wave_config.there_enemy())
    #handle inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #a proxima wave soh começa se escolher um poder
        for cards in cards_list:
            if cards.touched_power(event) and not wave_config.there_enemy():

                wave_config.set_can_spawn()
   
    delta_time = clock_obj.tick(60) / 1000
    #print(delta_time)
    #GUI CLOGIC AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    barlife.update(screen, player, wave_config)


def draw_game():
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))

    #drawing group
    player_group_sprite.draw(screen)

def actualize_groups_sprites():
    #usaremos mais tarde quando quiusermos colidir player e inimigp(xp) e balas tmb
    enemy_group_sprite = wave_config.get_group()
    bullet_group_sprite = player.get_bullets_sprite_group()
    #collisions handle
    colisions = pygame.sprite.groupcollide(enemy_group_sprite, bullet_group_sprite, False, True)
    for enemies, bullets in colisions.items():
        enemies.set_life(player.damage_fire)


pause = False
#loop of the paiagame
while(True):
    draw_game()
    update_game()
    #final
    
    clock_obj.tick(60)
    
    pygame.display.update()
    
    #GOSTARIA DE AGRADECER À PROFESSORA SENHORA RENATA, POIS DEVIDO A ELA CONSEGUI FAZER DE FORMA AUTÔNOMA A PARTE MATEMÀTICA DO JOGOOOOOOOOOOO ainnnnnnnnnnn
