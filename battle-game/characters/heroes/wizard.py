from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from gears.spell import Spell
from typing import Self
import functions
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class Wizard(Character) :
    MAX_HP = 150
    MAX_MANA = 55
    def __init__(self, name:str, weapon:Weapon, armor:Armor) -> None :
        Character.__init__(self, name, weapon, armor)
        self.hp = self.MAX_HP
        self.sorts = self.list_of_spells()
        self.mana = self.MAX_MANA
        self.alteration = 0
        self.speed = 10

    def __str__(self) -> None :
        """Show the main characteristics of the Wizard."""
        return f'{self.__class__.__name__} - {self.name} - HP : {self.MAX_HP}' \
               f' - Speed : {self.speed} - Mana : {self.MAX_MANA}'

    def list_of_spells(self) -> list[Spell]:
        """List that contains all the sorts of the Wizard."""
        fire = Spell('Fire', 40, 10)
        ice = Spell('Ice', 50, 15)
        return [fire, ice]
    
    def a_weapon(self, enemy:Self) -> None :
        """Attacks an enemy with a weapon."""
        functions.attack_msg(self, enemy, self.weapon.name)
        damage = self.weapon.damage
        functions.damages(enemy, damage)

    def a_spell(self, enemy:Self, spell_nb) -> None :
        """
        \nAttacks an enemy with one of the choosen spells.
        \nspell_nb = 1 or 2
        """
        # Gets the mana and the damage depending on the spell nb
        nb = 0 if (spell_nb == '1') else 1 # gets the spell nb
        mana = self.sorts[nb].mana # gets the mana
        print('\nMana ' + Fore.YELLOW + f'-{mana}')
        self.mana = self.mana - mana
        functions.attack_msg(self, enemy, self.sorts[nb].name)
        damage = self.sorts[nb].damage # gets the damage
        functions.damages(enemy, damage)

    def choose_attack(self, enemy:Self) -> None :
        """
        \nAsks the user what type of attack she.he prefers to choose :
        \n- weapon,
        \n- or spell.
        """
        print(Style.BRIGHT + Fore.CYAN + 
        '\nMANA : ' + Style.RESET_ALL + f'{self.mana}') # shows mana
        attack=''
        # shows weapon
        print(Style.BRIGHT + Fore.CYAN + '\nYOUR WEAPON :')
        self.weapon.show()
        # shows sorts
        print(Style.BRIGHT + Fore.CYAN + 'YOUR SORTS :')
        print(f'1. {self.sorts[0].__str__()}')
        print(f'2. {self.sorts[1].__str__()}')
        # Chooses the attack
        while (attack not in ('w', 's')) :
            print(Style.BRIGHT + Fore.BLACK + 
                  '\nDo you want to use your weapon or a spell... ? (w/s)')
            attack = input().lower()
            if (attack not in ('w', 's')) : 
                print(Fore.RED + 'You must enter \'w\' or \'s\'.')
        if (attack == 'w') : self.a_weapon(enemy) # choice = weapon
        # choice = spell
        elif (attack == 's') :
            if (self.mana >= 15) :
                spell = ''
                while (spell not in ('1', '2')) :
                    print(Style.BRIGHT + Fore.BLACK + 
                          '\nWhich spell do you want to use... ? (1/2)')
                    spell = input()
                    if (spell not in ('1', '2')) : 
                        print(Fore.RED + 'You must enter \'1\' or \'2\'.')
                self.a_spell(enemy, spell)
            else : self.a_spell(enemy, '1')
                        
    def attack(self, enemy:Self) -> None :
        super().attack(enemy)
        functions.check_status(self)
        if (functions.can_attack(self)) : 
            if (self.mana < 10) : self.a_weapon(enemy)
            else : self.choose_attack(enemy)