from cute_creature import CuteCreature

class EvolvableCuteCreature(CuteCreature):

    def __init__(self, level_up, new_species, type):
        CuteCreature.__init__(self, species, max_hp, attack_rating, defense_rating, xp_val, is_special = True)
        self.level_up = level_up
        self.new_species = new_species
        self.type = None

    def __str__(self):
        if self.type == None:
            return CuteCreature.__str__(self) + 'has no type'
        else:
            return CuteCreature.__str__(self.new_species) + f'{self.type}'

    def level_up_evol(self):
        if self.level == self.level_up:
            if 'A' <= CuteCreature.species[0] <= 'F':
                self.type = 'light'
            elif 'G' <= CuteCreature.species[0] <= 'L':
                self.type = 'dark'
            elif 'M' <= CuteCreature.species[0] <= 'R':
                self.type = 'nature'
            else:
                self.type = 'tech'
            CuteCreature.species = self.new_species
            print(f'{CuteCreature.species} is evolving into: {self.new_species} with new type: {self.type}')
        else:
            pass

    def special_attack(self, target):
        if self.type == None:
            print('Un-evolved creature can not use special attack.')
        elif self.type != None:
            if self.type == target.type:
                return CuteCreature.take_damage(0)
            elif (self.type == 'light' and target.type == 'tech') or (self.type == 'tech' and target.type == 'light'):
                if (self.attack_rating - 5 * target.defense_rating) < 0:
                    return CuteCreature.take_damage(0)
                else:
                    return CuteCreature.take_damage(self.attack_rating - 5 * target.defense_rating)
            elif (self.type == 'dark' and target.type == 'nature') or (self.type == 'nature' and target.type == 'dark'):
                if (self.attack_rating - 5 * target.defense_rating) < 0:
                    return CuteCreature.take_damage(0)
                else:
                    return CuteCreature.take_damage(self.attack_rating - 5 * target.defense_rating)
            else:
                if (5 * self.attack_rating - target.defense_rating) < 10:
                    return CuteCreature.take_damage(10)
                else:
                    return CuteCreature.take_damage(5 * self.attack_rating - target.defense_rating)
        else:
            return CuteCreature.take_damage(self.attack_rating - target.defense_rating)


if __name__ == '__main__':
    Eckanz = EvolvableCuteCreature(2, 'Dragon', None)
    Pikachu = EvolvableCuteCreature(2, 'Sloth', None)
    Eckanz.gain_xp(300)
    Pikachu.gain_xp(300)
    print(Eckanz)
