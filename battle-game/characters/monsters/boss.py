from characters.character import Character
from gears.weapon import Weapon
from gears.armor import Armor
from typing import Self
import functions
from random import randint
from colorama import init, Fore, Back, Style

# Initialiser colorama
init(autoreset=True)

class Boss(Character) :
    MAX_HP = 220
    def __init__(self, name:str='Shadow Puppeteer', weapon:Weapon=None, 
                 armor:Armor=None) -> None :
        Character.__init__(self, name, weapon, armor)
        self.hp = self.MAX_HP
        self.speed = 20

    def __str__(self) -> None :
        """Show the main characteristics of the Boss."""
        print(f'{self.name} - HP : {self.MAX_HP} - Speed : {self.speed}')
    
    def madness(self, enemy:Self) -> None :
        """
        \nAttack that drives the opponent crazy, so she.he can't attack
        \nduring one round.
        """
        functions.attack_msg(self, enemy, 'Madness')
        print(f'{enemy.name} descends into madness.')
        print(f'{enemy.name} will be enable to attack during one round.')
        enemy.alteration = 2
        functions.damages(enemy, 20)

    def darkness(self, enemy:Self) -> None :
        """
        \nThe boss uses this attack when the opponent is hit by 'Madness'
        \nattack.
        """
        functions.attack_msg(self, enemy, 'Darkness')
        functions.damages(enemy, 50)

    def injustice(self, enemy:Self) -> None :
        """
        \nAttack which removes 40 HP from the opponent and adds 40 HP to the
        \nboss.
        """
        functions.attack_msg(self, enemy, 'Injustice')
        damage = 40
        self.hp = self.hp + damage
        if (self.hp > self.MAX_HP) : self.hp = self.MAX_HP
        print(f'\n{self.name} ' + Fore.GREEN + f'+{damage} HP')
        functions.damages(enemy, damage)

    def claws(self, enemy:Self) -> None :
        """
        \nThe boss scratches the opponent.
        \nCan attack between one and three times.
        """
        functions.attack_msg(self, enemy, 'Claws')
        nb = randint(1,3)
        if nb == 1 : nbOfTimes = 'once'
        elif nb == 2 : nbOfTimes = 'twice'
        else : nbOfTimes = 'three times'
        print(f'{self.name} attacks ' + Fore.RED + f'{nbOfTimes}' + 
              Style.RESET_ALL + ' !')
        functions.damages(enemy, 25*nb)

    def attack(self, enemy:Self) -> None :
        super().attack(enemy)
        if (enemy.alteration > 0) : self.darkness(enemy)
        else :
            attack = [1,2,3][randint(0,2)] 
            if (attack == 1) : self.madness(enemy)
            elif (attack == 2) : self.injustice(enemy)
            else : self.claws(enemy)