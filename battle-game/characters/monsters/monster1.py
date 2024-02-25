from gears.spell import Spell
from gears.weapon import Weapon
from gears.armor import Armor
from characters.character import Character
from typing import Self
import functions
from random import randint
from colorama import Fore, Back, Style, init

# Initialize Colorama 
init(autoreset=True)

class Monster1(Character) :
    MAX_HP = 100
    def __init__(self, name:str='Alterplasma', weapon:Weapon=None, 
                 armor:Armor=None) -> None :
        Character.__init__(self, name, weapon, armor)   
        self.hp = self.MAX_HP
        self.speed = 5

    def __str__(self) -> None :
        """Show the main characteristics of the Monster1."""
        print(f'{self.name} - HP : {self.MAX_HP} - Speed : {self.speed}')
        
    def glutton(self, enemy:Self) -> None : 
        """Attack where the opponent looses 20 HP."""
        functions.attack_msg(self, enemy, 'Glutton')
        functions.damages(enemy, 20)

    def acid(self, enemy:Self) -> None :
        """
        \nThe monster throws acid at the opponent.
        \nCan attack between one and three times.
        """
        functions.attack_msg(self, enemy, 'Acid')
        nb = randint(1,3)
        if nb == 1 : nbOfTimes = 'once'
        elif nb == 2 : nbOfTimes = 'twice'
        else : nbOfTimes = 'three times'
        print(f'{self.name} attacks ' + Fore.RED + f'{nbOfTimes} ' + 
              Style.RESET_ALL + '!')
        functions.damages(enemy, 15*nb)


    def attack(self, enemy:Self) -> None :
        super().attack(enemy)
        attack = [1,2][randint(0,1)]
        if (attack == 1) : self.glutton(enemy)
        else : self.acid(enemy)