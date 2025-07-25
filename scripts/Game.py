#imports of that shit
import pygame
import random
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
number_control_wave = 0
#sound do menu
pygame.mixer.music.load('assets/sounds/music_menu.mp3')

background = pygame.image.load('assets/background.png')
player = Player()
wave_config = Wave()
barlife = Barlife()
menu = Menu_game()
lose = Menu_lose()
win = Menu_win()

clock_obj = pygame.time.Clock()
#lista para as cartas, o player vai poder escolher um a cada wave, sem poha de re roll
#tipos: range, max_life, cure, damage, velocity_move, velocity_attack
scale_card = 250
offset = 10
offset_card = scale_card + offset#pixseis
fixed_x = 0
fixed_y = 300
#lista root de cartas
cards_list = []
cards_list.append(Power('assets/cards/card_attack_range.png', 'range', (fixed_x,fixed_y), player, scale_card))
cards_list.append(Power('assets/cards/card_max_life.png', 'max_life', (fixed_x,fixed_y), player, scale_card))
cards_list.append(Power('assets/cards/card_cure.png', 'cure', (fixed_x, fixed_y), player, scale_card))
cards_list.append(Power('assets/cards/card_damage.png', 'damage', (fixed_x,fixed_y), player, scale_card))
cards_list.append(Power('assets/cards/card_velocity_move.png', 'velocity_move', (fixed_x,fixed_y), player, scale_card))
cards_list.append(Power('assets/cards/card_velocity_attack.png', 'velocity_attack', (fixed_x,fixed_y), player, scale_card))
#cartas selecionadas para escolher da lista root
list_cards_to_use = []
#cartas nao maximixadas
no_max_cards = []

#funcao para escolher 3 crtas aleatriias
def choices_cards():
    global offset
    global list_cards_to_use
    global cards_list

    #atualiza as cartas para ver se alguma é maximixada
    for i in range(len(cards_list)):
        cards_list[i].player = player
        cards_list[i].update_max() 


    offset = 10
    #comprensão de lista, pega somente as cartas nao maximizadas da lista root
    no_max_cards = [card for card in cards_list if not card.is_max]

    if len(no_max_cards) > 2:
        list_cards_to_use = random.sample(no_max_cards, 3)
    else:
        list_cards_to_use = random.sample(no_max_cards, 2)

        #debug
    for i in no_max_cards:
        print(i.my_type)
    print(' ##################################')
    for card in cards_list:
        card.set_position((10000,10000))
    
    for i in range(len(cards_list)):
        for j in range(len(list_cards_to_use)):
            if cards_list[i].my_type == list_cards_to_use[j].my_type:         
                cards_list[i].set_position((offset, fixed_y))
                offset += scale_card
    
choices_cards()

#group to actors
player_group_sprite = pygame.sprite.Group()
enemy_group_sprite = pygame.sprite.Group()
bullet_group_sprite = pygame.sprite.Group()

player_group_sprite.add(player)


#functions of game to paiagame 
def update_game():
    global delta_time
    global state
    global number_control_wave

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
        pygame.mixer.music.load('assets/sounds/music_won.mp3')
        state = 'won'


    #cartas
    for cards in cards_list:
        cards.update(screen, not wave_config.there_enemy())
    

   
    #handle inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #a proxima wave soh começa se escolher um poder
        #e soh pode ter um poder se nao houver inimigos tmb neh
        for cards in list_cards_to_use:
            if cards.touched_power(event,not wave_config.there_enemy()) and not wave_config.there_enemy(): 
                wave_config.set_can_spawn()

                if wave_config.number_wave != number_control_wave: 
                    choices_cards()
                    number_control_wave += 1
                    break
   
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
    #essa colisao ocorre com o grupo de balas do player com os inimigos
    colisions = pygame.sprite.groupcollide(enemy_group_sprite, bullet_group_sprite, False, True)
    for enemies, bullets in colisions.items():
        enemies.set_life(player.damage_fire)
    

#vou fazer uma function update geral pq to com medo de lascar tudo kakakakak
#ur dur tenho q evocar uma palavra reservada numa funcao PRA MUDAR UMA VARIAVEL GLOBAL
def update_general():
    global state
    global number_control_wave
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if menu.play(event):
            state = 'game'
        if lose.reset_touched(event):
            number_control_wave = 0
            print('reset')
            player.reset()
            wave_config.reset()
            state = 'game'
        #musica toca
        if not pygame.mixer.music.get_busy() and state != 'lose':
            pygame.mixer.music.play(-1)

#loop of the paiagame
while(True):

    match state:
        case 'menu':
            menu.update(screen)
            update_general()
            
        case 'game':
            draw_game()
            update_game()
            #musica para com fade
            pygame.mixer.music.fadeout(1000)
        case 'lose':
            lose.update(screen)
            update_general()

        case 'won':
            win.update(screen)
            update_general()
    #final
    
    clock_obj.tick(60)
    
    pygame.display.update()
    
#obg, prof Renata
#nah, odeio paiagame
#mdssssss to despendendo    tempo dms aq, tenho q estudar cálculo e geometria analiticaaaaaaaaaaaaaaaaaaaaaa
#love 2d é bem melhor, tipo x tendendo a 0 numa fração lá
