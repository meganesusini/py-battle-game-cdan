class Armor() :
    def __init__(self, name:str, defense:int, attack_bonus:int, 
                 speed_bonus:int) -> None :
        self.name = name
        self.defense = defense
        self.attack_bonus = attack_bonus
        self.speed_bonus = speed_bonus

    def __str__(self) -> None :
        """Shows all the characteristics of an armor."""
        return f'{self.name} - Defense : {self.defense} - Damage : ' \
               f'{self.attack_bonus} - Speed : {self.speed_bonus}'
        
    def show(self) -> None :
        """Shows only the main characteristics of an armor."""
        print(f'{self.name} - Defense : {self.defense}')

    