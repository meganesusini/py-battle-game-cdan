from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from colorama import init, Fore, Style
from random import randint

# Initialize colorama
init(autoreset=True)

def check_status(character:Character) -> None :
    """
    Checks if the character has an alteration.
    0 : no alteration,
    1 or 2 : alteration.
    """
    if (character.alteration > 0) :
        character.alteration = character.alteration - 1
        if (character.alteration == 1) :
            print(Fore.RED + f'\n{character.name} can\'t move.') 
        else :
            print(Fore.GREEN + 
                  f'\n{character.name}\'s stats are back to normal.\n')
    

def can_attack(character:Character) -> bool :
    """Checks if the character can attack or not."""
    if(character.hp <= 0 or character.alteration > 0) : return False
    else : return True


def damages(character:Character, damage:int) -> None :
    """Calculates the number of damage taken by a character.""" 
    # hero : hp -= (damage - defense)
    if (character.__class__.__name__ in ('Wizard', 'Barbarian')) :
        if (character.hp == character.MAX_HP) :
            print(Fore.CYAN + 
            f'\n{character.name}\'s {character.armor.name} protects the hero !')
            print(f'The power of the enemy attack is reduced by ' + 
            Fore.GREEN + f'{character.armor.defense}' + Style.RESET_ALL + 
            '.\n')
        damage = damage - character.armor.defense
        if (damage <= 0) :
            damage = 0
            print(Fore.GREEN + 
            f'\n{character.name} takes no damage thanks to the {character.armor.name}.')
    # monster : hp -= damage
    print(f'\n{character.name} ' + Fore.RED + f'-{damage} HP')

    character.hp = character.hp - damage


def attack_msg(attacker:Character, enemy:Character, attack_name:str) -> None :
    """Message when a character attacks."""
    if (attacker.__class__.__name__ in ('Wizard', 'Barbarian')) :
        print(Fore.CYAN + f'\n{attacker.name} ' + Style.RESET_ALL + 
        f'attacks ' + Fore.MAGENTA + f'{enemy.name}' + Style.RESET_ALL + 
        f' with {attack_name}.')
    else :
        print(Fore.MAGENTA + f'\n{attacker.name} ' + Style.RESET_ALL + 
        f'attacks ' + Fore.CYAN + f'{enemy.name}' + Style.RESET_ALL + 
        f' with {attack_name}.')


def upgrade(character:Character) -> None :
    """
    At the end of a fight, the hero can upgrade :
    - the HP,
    - the defense,
    - or the attack.
    The value of the upgrade is a random number between 5 and 10.
    """
    # The user chooses a stat to upgrade
    print(Style.BRIGHT + Fore.YELLOW + 
    '\nYou can upgrade a stat, the upgrade value will be a random number ' + 
    'between 5 and 10.')

    nb = ''
    while (nb not in ('1', '2', '3')) :
        print(Style.BRIGHT + Fore.BLACK + 
        '\nYou have to choose what do you to upgrade...')
        
        print('1. Your HP,\n2. Your defense,\n3. Your attack.')
        nb = input()
        if (nb not in ('1', '2', '3')) : 
            print(Fore.RED + 'You must enter a number between 1 and 3.')
    
    # The upgrade depending on the choosen stat
    random_value = randint(5,10)
    if (nb == '1') : 
        stat = 'HP'
        character.MAX_HP += random_value
    elif (nb == '2') :
        stat = 'defense'
        character.armor.defense += random_value
    else :
        stat = 'attack'
        character.weapon.damage += random_value
        if (character.__class__.__name__ == 'Wizard') :
            for spell in character.sorts :
                spell.damage += random_value

    print(Fore.GREEN + 
    f'\n{character.name}\'s {stat} has increased by {random_value}.')

    print(Fore.GREEN + 
    f'\nYou healed your hero, {character.name}\'s stats returned to normal.')


def show_heroes(list_of_heroes:list[Character]) -> None :
    """Shows the heroes that the user can choose."""
    print(Style.BRIGHT + Fore.CYAN + '\nHEROES :')
    nb = 1
    
    for h in list_of_heroes :
        h_class = h.__class__.__name__
        if (h_class == 'Wizard') :
            print(f'{nb}. ' + h.__str__())
            print(Style.BRIGHT + Fore.CYAN + 'SPECIAL : A Wizard can use sorts : ')
            for s in h.sorts :
                print(f'{s.__str__()}')
        else : 
            print(f'{nb}. ' + h.__str__())
            print(Style.BRIGHT + Fore.CYAN + 
                  'SPECIAL : A Barbarian attacks twice.')
        nb+=1


def show_weapons(list_of_weapons:list[Weapon]) -> None :
    """Shows the weapons that the user can choose."""
    print(Style.BRIGHT + Fore.BLUE + '\nWEAPONS :')
    nb=1
    for w in list_of_weapons :
        print(f'{nb}. ' + w.__str__())
        nb+=1


def show_armors(list_of_armors:list[Armor]) -> None :
    """Shows the armors that the user can choose."""
    print(Style.BRIGHT + Fore.MAGENTA + '\nARMORS :')
    nb=1
    for a in list_of_armors :
        print(f'{nb}. ' + a.__str__())
        nb+=1


def create_hero(hero_class:str, hero_name:str, list_of_weapons:list[Weapon], 
                list_of_armors:list[Armor]) -> list :
    """Create a hero by giving her.him :
    - a name,
    - a weapon,
    - and an armor.
    """

    # Chooses a weapon and an armor
    for i in range(0,2) :

        if (i == 0) : 
            gears = list_of_weapons
            element = 'weapon'
        else : 
            gears = list_of_armors
            element = 'armor'

        list_of_elements = [str(i) for i in range(1, len(gears)+1)]
        element_nb = ''

        while (element_nb not in list_of_elements) :

            print(Style.BRIGHT + Fore.BLACK + 
            f'\nChoose {'a' if element=='weapon' else 'an'} {element} for ' + 
            f'the {hero_class} (1-{len(gears)})...')

            element_nb = input()

            if (element_nb not in list_of_elements) : 
                print(Fore.RED + 
                f'\nYou must enter a number between 1 and {len(gears)}.')

        element_nb = int(element_nb) - 1
        element = gears[element_nb]

        if (i == 0) : weapon = element
        else : armor = element

    return [hero_class, hero_name, weapon, armor]


def choose_hero(h_list:list[Character]) -> str :
    """The user chooses the hero he wants to send into battle."""
    hero = ''
    numbers = [str(i) for i in range(1, len(h_list)+1)]

    while (hero not in numbers) :
        print(Style.BRIGHT + Fore.BLACK + 
        f'\nWhich hero do you want to send into battle ? (1-{len(h_list)})')
        hero = input()
        if (hero not in numbers) : 
            print(Fore.RED + f'\nYou must enter a number between 1 and {len(h_list)}.')
    hero = int(hero)-1

    if(h_list[hero].__class__.__name__ == 'Wizard') : 
        print(Style.BRIGHT + Fore.BLACK + '\nYou have choosen the Wizard...')
        return 'Wizard'
    else : 
        print(Style.BRIGHT + Fore.BLACK + '\nYou have choosen the Barbarian...')
        return 'Barbarian'
    
def add_weapon_armor_stat_bonus(hero:Character) :
    """
    \nAdd the bonus to your hero depending on the armor and weapon choosen.
    \nShows the upgrade."""
    # Add bonus
    speed_bonus = hero.weapon.speed_bonus + hero.armor.speed_bonus
    hero.speed += speed_bonus
    attack_bonus = hero.armor.attack_bonus
    hero.weapon.damage += attack_bonus
    # Shows upgrade
    if (speed_bonus >= 0) : 
        speed_color = Fore.GREEN
        speed_bonus = '+' + str(speed_bonus)
    else : 
        speed_color = Fore.RED
        speed_bonus = str(speed_bonus)
    if (attack_bonus >= 0) : 
        damage_color = Fore.GREEN
        damage_bonus = '+' + str(attack_bonus)
    else : 
        damage_color = Fore.RED
        damage_bonus = str(attack_bonus)
    print(Fore.GREEN + f'\nThe choice of your weapon and your armor has modified your stats :')
    print(Style.BRIGHT + Fore.CYAN + '\nYOUR HERO :')
    if (hero.__class__.__name__ == 'Wizard') :
        for spell in hero.sorts : spell.damage += attack_bonus
        print(f'{hero.__class__.__name__} : {hero.name} - HP : {hero.MAX_HP} - Speed : {hero.speed} [' + speed_color + f'{speed_bonus}' + Style.RESET_ALL + f'] - Mana : {hero.MAX_MANA}')
        print(Style.BRIGHT + Fore.CYAN + f'YOUR SORTS :')
        for spell in hero.sorts :
            print(f'{spell.name} - Damage : {spell.damage} [' + damage_color + f'{damage_bonus}' + Style.RESET_ALL + f'] - Mana : {spell.mana}')
    else :
        print(f'{hero.__str__()} [' + speed_color + f'{speed_bonus}' + Style.RESET_ALL + f']')
    print(Style.BRIGHT + Fore.CYAN + f'YOUR WEAPON :')
    print(f'{hero.weapon.name} - Damage : {hero.weapon.damage} [' + damage_color + f'{damage_bonus}' + Style.RESET_ALL + f']')
    print(Style.BRIGHT + Fore.CYAN + f'YOUR ARMOR :')
    print(f'{hero.armor.name} - Defense : {hero.armor.defense}')
    
