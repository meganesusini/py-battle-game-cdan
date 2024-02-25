from characters.character import Character
from gears.spell import Spell
from typing import Self
import functions
from random import randint

class Monster4(Character) :
    MAX_HP = 150
    def __init__(self, name:str='Nightmare Shadow', weapon=None, armor=None) -> None :
        Character.__init__(self, name, weapon, armor)
        self.hp = self.MAX_HP
        self.speed = 10

    def __str__(self) -> None :
        """Show the main characteristics of the Monster3."""
        print(f'{self.name} - HP : {self.MAX_HP} - Speed : {self.speed}')

    def fear(self, enemy:Self) -> None :
        """
        \nAttack : Scare the opponent.
        \nThe opponent looses 20 HP.
        """
        functions.attack_msg(self, enemy, 'Fear')
        print(f'{enemy.name} is paralyzed by fear.')
        print(f'{enemy.name} will be afraid during one round.')
        enemy.alteration = 2
        functions.damages(enemy, 20)

    def phobia(self, enemy:Self) -> None :
        """
        \nAttack : Use this attack when the opponent is afraid.
        \nThe opponent looses 45 HP.
        """
        functions.attack_msg(self, enemy, 'Phobia')
        functions.damages(enemy, 45)

    def insomnia(self, enemy:Self) -> None :
        """Attack where the opponent looses 40 HP."""
        functions.attack_msg(self, enemy, 'Insomnia')
        functions.damages(enemy, 40)

    def attack(self, enemy:Self) -> None :
        super().attack(enemy)
        if (enemy.alteration > 0) : 
            self.phobia(enemy)
        else :
            attack = [1,2][randint(0,1)] 
            if (attack == 1) : self.fear(enemy)
            else : self.insomnia(enemy)