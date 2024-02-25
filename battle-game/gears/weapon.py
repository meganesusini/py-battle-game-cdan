class Weapon() :
    def __init__(self, name:str, damage:int, speed_bonus:int) -> None :
        self.name = name
        self.damage = damage
        self.speed_bonus = speed_bonus

    def __str__(self) -> None :
        """Shows all the characteristics of a weapon."""
        return f'{self.name} - Damage : {self.damage} - Speed : ' \
               f'{self.speed_bonus}'

    def show(self) -> None :
        """Shows only the main characteristics of a weapon."""
        print(f'{self.name} - Damage : {self.damage}')
