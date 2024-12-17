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
    
    def fight(self, opponent):
        print(self.name, 'encountered', opponent.name)
        print(self.name, 'VS', opponent.name)
        print('FIGHT')
        print(self.name, 'attacks', opponent.name, 'with', self.weapon)
        print(opponent.name, 'took damage.')
        qoldi = opponent.armor - self.power
        if qoldi >= 0:
            print('His armor: ', qoldi, 'and His health: ', opponent.health)
        elif qoldi <=0:
            print(opponent.health - self.power, '\n')

warrior1 = Warrior('P.E.K.K.A', 5000, 5000, 'sword', 2000)
warrior2 = Warrior('Golem', 6000, 6000, 'hands', 1000)
warrior1.show()
warrior2.show()
warrior1.fight(warrior2)
warrior2.fight(warrior1)
