from characters.character import Character
from colorama import Fore, Style, init

# Initialize Colorama 
init(autoreset=True)

class Arena :
    def __init__(self, hero:Character, monster:Character) -> None :
        self.hero = hero
        self.monster = monster

    def speed_order(self, hero:Character, monster:Character) -> list[Character] :
        """Returns the order of attack in a fight depending on the speed of 
        each fighter."""
        if (hero.speed >= monster.speed) : return [hero, monster]
        else : return [monster, hero]

    # Display the results of the round
    def round_result(self) -> None :
        """Shows the fighter's stats after a round."""
        # Check the HP
        if(self.hero.hp < 0) : self.hero.hp = 0
        if(self.monster.hp < 0) : self.monster.hp = 0
        # Shows the results
        print(Style.BRIGHT + Fore.WHITE + "\nRESULTS:")
        print('\n[' + Fore.CYAN + f'{self.hero.name} ' + Style.RESET_ALL + 
              f': {self.hero.hp} / {self.hero.MAX_HP} HP] | [' + 
              Fore.MAGENTA + f'{self.monster.name} ' + Style.RESET_ALL + 
              f': {self.monster.hp} / {self.monster.MAX_HP} HP]\n')
        input("------------------\n")

    def fight(self) -> None :   
        """Shows the fight between the monster and the hero."""
        # Choose which character will attack first
        attacker = self.speed_order(self.hero, self.monster)[0]
        enemy = self.speed_order(self.hero, self.monster)[1]
        # Fight
        while (self.hero.hp > 0 and self.monster.hp > 0) :
            attacker.attack(enemy)
            self.round_result()
            attacker = self.monster if (attacker == self.hero) else self.hero
            enemy = self.hero if (attacker == self.monster) else self.monster

        # Check who is KO
        dead = self.monster if (self.hero.hp > 0) else self.hero

        # Shows the final results for the hero
        if (dead.__class__.__name__ in ('Wizard', 'Barbarian')) :
            print(Fore.RED + f'\n{dead.name} is KO.')
        else :
            print(Fore.GREEN + f'\nWell done ! {self.hero.name} defeated ' + 
                  'the monster !')