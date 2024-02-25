class Spell :
    def __init__(self, name, damage, mana) -> None :
        self.name = name
        self.damage = damage
        self.mana = mana

    def __str__(self) -> str :
        """Shows all the characteritics of a spell."""
        return f'{self.name} - Damage : {self.damage} - Mana : {self.mana}'