import random

'''
A video game where the objective is to travel around the world collect-
ing cute cartoonish creatures that become stronger over time by fighting other cute cartoonish creatures.
'''


class CuteCreature:

    # initializes CuteCreature instance methods
    def __init__(self, species, max_hp, attack_rating, defense_rating, xp_val, is_special=True):
        self.species = species
        self.level = 1
        self.curr_hp = max_hp
        self.max_hp = max_hp
        self.attack_rating = attack_rating
        self.defense_rating = defense_rating
        self.xp = 0
        self.xp_val = xp_val
        self.is_special = is_special
        self.next_level_xp = 200

    # Returns a string summarizing all the instance attributes of the CuteCreature
    def __str__(self):
        if self.is_special:
            return f'Level {self.level} {self.species}\n***Special***\nHP:     {self.curr_hp}/{self.max_hp}\nATK:    {self.attack_rating}\n' \
                   f'DEF:    {self.defense_rating}\nXP:     {self.xp}/{self.next_level_xp}\nXP Val: {self.xp_val}'
        else:
            return f'Level {self.level} {self.species}\n***Not Special***\nHP:     {self.curr_hp}/{self.max_hp}\nATK:    {self.attack_rating}\n' \
                   f'DEF:    {self.defense_rating}\nXP:     {self.xp}/{self.next_level_xp}\nXP Val: {self.xp_val}'

    # Makes the CuteCreature level up
    def level_up(self):
        self.level += 1
        self.next_level_xp += 75
        print(f'{self.species} + 200 XP  |  Level: {self.level}')
        if self.level >= 2 and self.level <= 9:
            self.max_hp += 7
            self.attack_rating += 3
            self.defense_rating += 3
        elif self.level >= 10:
            self.max_hp += 2
            self.attack_rating += 1
            self.defense_rating += 1
        self.xp_val += 25
        self.curr_hp = self.max_hp

    # CuteCreature gains xp and calls level up when needed
    def gain_xp(self, amount):
        if amount >= 0:
            print(f'{self.species} gained {amount} experience!')
            self.xp += amount
            level_increase = self.xp // self.next_level_xp
            new_xp = self.xp - (level_increase * self.next_level_xp)
            for level in range(level_increase):
                self.level_up()
            self.xp = new_xp

    # CuteCreature takes damage and outputs hp
    def take_damage(self, amount):
        if amount > self.curr_hp:
            self.curr_hp = 0
            print(f'Damage Taken: -', amount, f',{self.species} HP: {self.curr_hp}/{self.max_hp}')
        else:
            self.curr_hp -= amount
            print(f'Damage Taken: -', amount, f',{self.species} HP: {self.curr_hp}/{self.max_hp}')

    # CuteCreatures attack each other and the required method is called
    def attack(self, target):
        print(f'{self.species} is attacking {target.species}')
        if target.curr_hp == 0:
            print(f'{self.species} has defeated {target.species}')
            self.gain_xp(target.xp_val)
        random_chance = random.randint(1, 100)
        if random_chance <= 70:
            print('Hit!')
            damage = self.attack_rating - target.defense_rating
            if damage >= 1:
                target.take_damage(damage)
            else:
                target.take_damage(1)
        elif random_chance >= 71 and random_chance <= 80:
            print('Critical Hit!')
            damage = (self.attack_rating - target.defense_rating) * 2
            if damage >= 2:
                target.take_damage(damage)
            else:
                target.take_damage(2)
        else:
            print('Miss!')
        if target.curr_hp == 0:
            print()
            print(f'{self.species} has defeated {target.species}!')
            self.gain_xp(target.xp_val)


if __name__ == '__main__':
    Eckanz = CuteCreature('Eckanz', 100, 6, 8, 350, True)
    Pikachu = CuteCreature('Pikachu', 100, 18, 3, 300, True)

    print(Eckanz)
    print(Pikachu)

    # Returns the result of each CuteCreature attack
    while Eckanz.curr_hp > 0 and Pikachu.curr_hp > 0:
        CuteCreature.attack(Pikachu, Eckanz)
        print()
        if Eckanz.curr_hp == 0:
            break
        CuteCreature.attack(Eckanz, Pikachu)
        print()

    print(Eckanz)
    print(Pikachu)
