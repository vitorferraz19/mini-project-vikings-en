import random

# Soldier


class Soldier:
    def __init__(self, health, strength):   # constructor function with 2 arguments: health and strength
        self.health = health           # receives the health property as its 1st argument
        self.strength = strength         # receives the strength property as its 2nd argument
    
    def attack(self):   # 0 arguments
        return self.strength    # returns the strength property of the Soldier class

    def receiveDamage(self, damage):   # receives 1 argument (the damage)
        self.health -= damage    # removes the received damage from the health property


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)    # inheriting these from the Soldier class
        self.name = name      # adding additional name attribute (specific to this class)

    def battleCry(self):   # 0 arguments
        return "Odin Owns You All!"               # message returned in this case

    def receiveDamage(self, damage):    # 1 argument: damage
        self.health -= damage                # removes the received damage from the health property
        if self.health > 0:          # assuming the Viking is alive
            return f"{self.name} has received {damage} points of damage"    # returning this message on points of damage
        else:
            return f"{self.name} has died in act of combat"     # otherwise, returning this message

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)   # inheriting these from the Soldier class

    def receiveDamage(self, damage):      # 1 argument: damage
        self.health -= damage        # removes the received damage from the health property
        if self.health > 0:           # assuming the Saxon is alive
            return f"A Saxon has received {damage} points of damage"   # returning this message on points of damag
        else:
            return "A Saxon has died in combat"   # otherwise, returning this message
""""
# Davicente

class War():
    def __init__(self):
        # your code here

    def addViking(self, viking):
        # your code here
    
    def addSaxon(self, saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here
    
    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here
    pass

"""
