from django.shortcuts import render, HttpResponse

from random import uniform, choice

class StudentFighter(object):

    def __init__(self, strength, health, name, specials):
        self.strength = strength
        self.name = name
        self.health = health

        self.specials = specials



    def attack(self, opponent):
        multiplier = uniform(0.3,1.3)

        the_attack = choice(self.specials)
        attack_name = the_attack[0]
        damage = the_attack[1]

        damage = int(multiplier * damage)
        opponent.health -= damage

        message_one = "{} used {}. ".format(self.name, attack_name)
        message_one += "A successful attack! {} Damage points!".format(damage)

        if multiplier > 2:
            message_one += " Critical Damage!"

        if opponent.health > 0:
            # if opponent still has health points simply
            # show how many left
            message_two = "{} has {} health points remaining".format(opponent.name, opponent.health)
        else:
            # if opponent has none left show they have fainted.
            message_two = "{} has fainted. You win!".format(opponent.name)
        return message_one, message_two

kalu_specials = [("Enchanter's Song", 4), ('Dream Erupter', 5), ("Wizard O'War", 3),
                 ('Whirlwind Dash', 8), ("Spirit of Brutus", 6), ("Mother's Kiss", 15),
                 ("Frantic Finisher", 5), ("Philosopher's Scowl", 12), ("The Forgiveness Dance", 13)]
david_specials = [('iceball', 3), ('whispering scream', 5)]

kalu = StudentFighter(strength=3, health=100, name="Kalu", specials=kalu_specials)
david = StudentFighter(strength=5, health=100, name="David", specials=david_specials)

kalu.attack(david)
def home(self):
    return HttpResponse(kalu.attack(david))
