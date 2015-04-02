#!/usr/bin/env python
import random

class Animal:
    legs = 4
    eyes = 2
    mouth = 1
    dead = False
    
class Spider(Animal):
    def __init__(self, legs = 8, eyes = 12, size = "small", name="default Spider"):
        self.legs = legs
        self.eyes = eyes
        self.size = size
        self.name = name
        self.hp = 10

    def skitter(self):
        if not self.dead:
            print "Skitter skitter."
        else:
            print "Dead spiders don't skitter..."

    def squish(self):
        self.dead = True
        print "%s splattered all over the place" % self.name

Joe = Spider(legs = 7, name = "Joey Seven Leggs")
Billy = Spider(name = "Billy")

def attack(attacker, defender):
    print "%s attacks %s" % (attacker.name, defender.name)
    damage = random.randint(0,3)
    print "%s takes %s damage" %(defender.name, damage)   
    defender.hp -= damage

Billy.skitter()
Billy.skitter()
Billy.squish()
Billy.skitter()

while Joe.hp >= 0 or Billy.hp >= 0:
    attack(Billy, Joe)
    attack(Joe, Billy)


