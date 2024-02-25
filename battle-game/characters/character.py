from gears.weapon import Weapon
from gears.armor import Armor
from typing import Self
from abc import ABC, abstractmethod 


class Character(ABC) :
    @abstractmethod
    def __init__(self, name:str, weapon:Weapon, armor:Armor) -> None :
        self.name = name
        self.weapon = weapon
        self.armor = armor

    def attack(self, enemy:Self) -> None :
        """Attacks an enemy with a spell or a weapon."""
        pass

    
