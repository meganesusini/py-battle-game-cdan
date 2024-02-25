from characters.character import Character
from random import randint

class Room() :
    def __init__(self, hero:Character, monsters:list[Character]) -> None:
        self.hero = hero
        self.monsters = monsters

    def monster_in_room(self, nb:int) -> Character :
        """Chooses a monster at random based on the room number."""
        m1_list = []
        m2_list = []
        boss = ""
        for m in self.monsters :
            if (m.__class__.__name__ in ('Monster1', 'Monster2')) : 
                m1_list.append(m)
            elif (m.__class__.__name__ == 'Boss') : boss = m
            else : m2_list.append(m)
        if (nb == 1) : return m1_list[randint(0,1)]
        elif (nb == 2) : return m2_list[randint(0,1)]
        else : return boss