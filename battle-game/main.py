
from gears.weapon import Weapon
from gears.armor import Armor
from characters.heroes.barbarian import Barbarian
from characters.heroes.wizard import Wizard
from characters.monsters.monster1 import Monster1
from characters.monsters.monster2 import Monster2
from characters.monsters.monster3 import Monster3
from characters.monsters.monster4 import Monster4
from characters.monsters.boss import Boss
from map.map import Map
import functions
from colorama import Fore, Style, init

# Initialise Colorama 
init(autoreset=True)

# weapons
sword = Weapon('Sword', 15, 0) 
blade = Weapon('Blade', 10, 10) 
axe = Weapon('Axe', 20, -10) 
spear = Weapon('Spear', 15, 5) 

# armors
magic_ring = Armor('Magic Ring', 20, -10, 0) 
shield = Armor('Shield', 20, 0, -5) 
bewitched_cape = Armor('Bewitched Cape', 10, 5, 5)
dragon_skin_suit = Armor('Dragon Skin Suit', 15, 5, -5) 

# monsters
m1 = Monster1()
m2 = Monster2()
m3 = Monster3()
m4 = Monster4()
b = Boss()

m_list = [m1, m2, m3, m4, b]

h_list = [Barbarian('[Barbarian name]', None, None), 
          Wizard('[Wizard name]', None, None)]

w_list = [sword, blade, axe, spear]

a_list = [magic_ring, shield, bewitched_cape, dragon_skin_suit]

# Context
print(Style.BRIGHT + Fore.MAGENTA + '\nWELCOME IN BATTLE GAME\n')
print('You are a hero, you can be a wizard or a barbarian.')
print('You are in a map that contains 3 rooms.')
print('In each room, there is a monster you must fight.')
print('The next room is more difficult than the previous one.')
print('The goal is to win the battle against all the monsters and the boss ' + 
      'that is in the third room.\n')
print(Style.BRIGHT + Fore.BLUE + 'Are you ready ? ' + Fore.WHITE + 'GO !\n\n')
print(Style.BRIGHT + Fore.BLACK + 'First, you have to customize your heroes...')
answer = ''
hero = ''

# Custom hero
while (answer != 'yes') :
    answer = ''
    functions.show_heroes(h_list)
    hero_class = functions.choose_hero(h_list)
    # Chooses a name
    print(Style.BRIGHT + Fore.BLACK + f'\nChoose a name for the {hero_class}...')
    hero_name = input()
    functions.show_weapons(w_list)
    functions.show_armors(a_list)
    hero = functions.create_hero(hero_class, hero_name, w_list, a_list)
    print(Style.BRIGHT + Fore.BLACK + f'You have choosen a ' + Fore.WHITE + 
          f'{hero[0]}' + Fore.BLACK + f' called ' + Fore.WHITE + f'{hero[1]}' + 
          Fore.BLACK + f', and who wears a ' + Fore.WHITE + f'{hero[2].name}' + 
          Fore.BLACK + f' and a ' + Fore.WHITE + f'{hero[3].name}' + Fore.BLACK + 
          '.')
    while (answer not in ['yes', 'no']) :
        print(Style.BRIGHT + Fore.BLACK + '\nThat\'s it ? (yes/no)')
        answer = input().lower()
        if (answer not in ['yes', 'no']) : 
             print(Fore.RED + '\nYou must enter \'yes\' or \'no\'.')

# Create hero
if (hero[0] == 'Wizard') : hero = Wizard(hero[1], hero[2], hero[3])
else : hero = Barbarian(hero[1], hero[2], hero[3])
functions.add_weapon_armor_stat_bonus(hero)

# Send hero to fight
map = Map(hero, m_list)
map.start()