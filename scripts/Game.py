#imports of that shit
import pygame
from Wave import Wave
from GUI import Barlife, Menu_game, Menu_lose, Menu_win
from actors.Player import Player
from Powers import Power
#init of game
pygame.init()

pygame.mixer.init(44100, -16,2,2048)
#variables
#states: menu, game, dead
state = 'menu'
delta_time = 0
width_screen = 800
height_screen = 600
screen = pygame.display.set_mode((width_screen, height_screen), pygame.RESIZABLE | pygame.SCALED)
pygame.display.set_caption('60 WAVES WITH FREDERICO')
#sound
pygame.mixer.music.load('assets/sounds/music_menu.mp3')

background = pygame.image.load('assets/background.png')
player = Player()
wave_config = Wave()
barlife = Barlife()
menu = Menu_game()
lose = Menu_lose()
win = Menu_win()

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
    global state
    #wave config
    player.update_game(screen, wave_config.nearest_enemy(player), wave_config.there_enemy(), delta_time)
    wave_config.update(screen, player, delta_time)
    #updating group
    player_group_sprite.update(screen)
    actualize_groups_sprites()
    #se player morrer muda estado
    if not player.is_alive():
        state = 'lose'
    #se cehgar a wave 60 e n tiver inimigod venceu
    if wave_config.number_wave > 59 and not wave_config.there_enemy():
        state = 'winned'

    #cartas
    for cards in cards_list:
        cards.update(screen, not wave_config.there_enemy())
    #handle inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #a proxima wave soh começa se escolher um poder
        #e soh pode ter um poder se nao houver inimigos tmb neh
        for cards in cards_list:
            if cards.touched_power(event,not wave_config.there_enemy()) and not wave_config.there_enemy():

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

#vou fazer uma function update geral pq to com medo de lascar tudo kakakakak
#ur dur tenho q evocar uma palavra reservada numa funcao PRA MUDAR UMA VARIAVEL LLOCAL MDSSSS
def update_general():
    global state
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if menu.play(event):
            state = 'game'
        if lose.reset_touched(event):
            print('reset')
            player.reset()
            wave_config.reset()
            state = 'game'

#loop of the paiagame
while(True):

    match state:
        case 'menu':
            menu.update(screen)
            update_general()
            #musica do menu toca
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)
        case 'game':
            draw_game()
            update_game()
            #musica para com fade
            pygame.mixer.music.fadeout(1000)
        case 'lose':
            lose.update(screen)
            update_general()

        case 'winned':
            win.update(screen)
            update_general()
    #final
    
    clock_obj.tick(60)
    
    pygame.display.update()
    
    #GOSTARIA DE AGRADECER À PROFESSORA SENHORA RENATA, POIS DEVIDO A ELA CONSEGUI FAZER DE FORMA AUTÔNOMA A PARTE MATEMÀTICA DO JOGOOOOOOOOOOO ainnnnnnnnnnn
#nah, odeio paiagame
#mdssssss to despendendo    tempo dms aq, tenho q estudar cálculo e geometria analiticaaaaaaaaaaaaaaaaaaaaaa
#love 2d é bem melhor, tipo x tendendo a 0 e sobre 1