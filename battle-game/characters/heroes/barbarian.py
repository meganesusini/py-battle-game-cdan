from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from typing import Self
import functions
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

class Barbarian(Character) :
    MAX_HP = 150
    def __init__(self, name:str, weapon:Weapon, armor:Armor) -> None :
        Character.__init__(self, name, weapon, armor)
        self.hp = self.MAX_HP
        self.alteration = 0
        self.speed = 10

    def __str__(self) -> None :
        """Show the main characteristics of the Barbarian."""
        return f'{self.__class__.__name__} - {self.name} - HP : {self.MAX_HP} ' \
               f'- Speed : {self.speed}'

    def attack(self, enemy:Self) -> None :
        super().attack(enemy)
        functions.check_status(self)
        if (functions.can_attack(self)) : 
            print(Style.BRIGHT + Fore.CYAN + '\nYOUR WEAPON :')
            self.weapon.show()
            functions.attack_msg(self, enemy, self.weapon.name)
            print(f'The barbarian hits ' + Fore.RED + 'twice ' + 
                  Style.RESET_ALL  + '!')
            damage = self.weapon.damage * 2
            functions.damages(enemy, damage)
        