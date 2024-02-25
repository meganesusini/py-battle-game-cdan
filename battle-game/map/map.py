from characters.character import Character
from map.room import Room
from map.arena import Arena
from colorama import Fore, Style, init
import functions

# Initialize Colorama
init(autoreset=True)

class Map() :
    def __init__(self, hero:Character, monsters:list[Character]) -> None:
        self.hero = hero
        self.monsters = monsters

    def start(self) -> None :
        """
        \nThe hero starts the battle.
        \nShe.he has to fight all the monsters in the map.
        """
        room = Room(self.hero, self.monsters)
        nb = 1
        while (self.hero.hp > 0 and nb < 4) :
            if (nb == 1) : word = 'first'
            elif (nb == 2) : word = 'second'
            else : word = 'third and last'
            print(Style.BRIGHT + Fore.BLACK + f'\n{self.hero.name} enters in the {word} room...')
            print(Style.BRIGHT + Fore.BLUE + f'\n\nROOM {nb}')
            monster = room.monster_in_room(nb)
            # Shows the caracteristics of the monster
            print(Style.BRIGHT + Fore.MAGENTA + '\nYOUR OPPONENT :')
            monster.__str__()
            
            # Start of the fight
            arena = Arena(self.hero, monster)
            arena.fight()

            if (self.hero.hp <= 0) :
                # Case when the hero is KO
                print(Fore.RED + f'\nThe fight is finished for {self.hero.name}.')
                break
            else :
                if (nb < 3) :
                    # Case when the hero win a fight, so she.he can 
                    # upgrade her.his stats
                    print()
                    functions.upgrade(self.hero)
                    print()
                    self.hero.hp = self.hero.MAX_HP
                    self.hero.alteration = 0
                    if (self.hero.__class__.__name__ == 'Wizard') : 
                        self.hero.mana =self.hero.MAX_MANA
                    else :
                        if (self.hero.hp <= 0) :
                            print(Fore.RED + f'\nYou won the game !')
                nb+=1
            
        print(Style.BRIGHT + Fore.YELLOW + '\nEND')