from characters.character import Character
from typing import Self
import functions
from random import randint

class Monster3(Character) :
    MAX_HP = 150
    def __init__(self, name:str='Dream Eater', weapon=None, armor=None) -> None :
        Character.__init__(self, name, weapon, armor)
        self.hp = self.MAX_HP
        self.speed = 10

    def __str__(self) -> None :
        """Show the main characteristics of the Monster3."""
        print(f'{self.name} - HP : {self.MAX_HP} - Speed : {self.speed}')

    def sleep(self, enemy:Self) -> None :
        """Attack : Gets the opponent to sleep during one round."""
        functions.attack_msg(self, enemy, 'Sleep')
        print(f'\n{enemy.name} is falling asleep.')
        print(f'{enemy.name} will sleep during one round.')
        enemy.alteration = 2
        functions.damages(enemy, 20)

    def eat_dreams(self, enemy:Self) -> None :
        """Attack : Uses this attack when the opponent is asleep."""
        functions.attack_msg(self, enemy, 'Eat Dreams')
        functions.damages(enemy, 45)

    def weaking_nightmare(self, enemy:Self) -> None :
        """Attack where the opponent looses 40 HP."""
        functions.attack_msg(self, enemy, 'Weaking Nightmare')
        functions.damages(enemy, 40)

    def attack(self, enemy:Self) -> None :
        super().attack(enemy)
        if (enemy.alteration > 0) : 
            self.eat_dreams(enemy)
        else : 
            attack = [1,2][randint(0,1)] 
            if (attack == 1) : self.sleep(enemy)
            else : self.weaking_nightmare(enemy)