class Warrior():
    def __init__(self, name, health, armor, weapon, power):
        self.name = name
        self.health = health
        self. armor = armor
        self.weapon = weapon
        self.power = power

    def show(self):
        print('Greet the hero - ', self.name)
        print('Health: ', self.health)
        print('Armor: ', self.armor)
        print('Weapon: ', self.weapon)
        print('Power: ', self.power, '\n')
