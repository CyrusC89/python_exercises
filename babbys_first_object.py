#!/usr/bin/env python

class Person:
    legs = 2
    def __init__(self, name, height, weight, age, hunger):
        self.first_name, self.last_name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.hunger = hunger
        self.dead = False

    def eat(self, food="slop", value=10):
        if not self.dead:
            print "%s ate %s" % (self.first_name, food)
            self.hunger += value
        else:
            self.is_dead()

    def poop(self, location, preposition="on"):
        if not self.dead:
            print "%s took a huge dump %s %s" % (self.first_name, preposition, location)
            self.hunger -= 10
            self.check_stats()
        else:
            self.is_dead()

    def vomit(self):
        print "%s vomits profusely on the ground" % self.first_name
        self.hunger -= 50

    def level_up(self):
        if not self.dead:
            self.age += 1
            print "%s is now %s years old" % (self.first_name, self.age)
        else:
            self.is_dead()

    def bio(self):
        print "=" * 20
        print "%s %s" % (self.first_name, self.last_name)
        if self.dead:
            print "Died at the sweet, sweet age of %s" % self.age
        else:
            print "Age %s" % self.age
        print "%scm in height, %skg" % (self.height, self.weight)
        self.check_stats()

    def death(self, reason):
        self.dead = True
        print "Oh no, %s has died of %s" % (self.first_name, reason)

    def check_stats(self):
        if self.hunger <= 0:
            self.death("starvation")
        elif self.hunger <= 10:
            print "%s is really close to starving!" % self.first_name
        elif self.hunger <= 20:
            print "%s is really hungry!" % self.first_name
        elif self.hunger <= 30:
            print "%s is hungry!" % self.first_name
        elif self.hunger >= 200:
            self.death("stomach rupture")
        elif self.hunger >= 110:
            self.vomit()
        elif self.hunger > 70:
            print "%s is painfully bloated. Ew." % self.first_name

    def is_dead(self):
        print "%s can't do anything because they are dead" % self.first_name


def main():
    Seth = Person(("Seth", "Moore"), 160, 100, 26, 30)
    Cyrus = Person(("Cyrus", "Conner"), 125, 125, 30, 10)

    Cyrus.poop("Mallory's mouth", preposition="in")
    
    Seth.bio()
    Seth.level_up()
    Seth.bio()
    Seth.eat()
    Seth.eat("turkey and mashed potato dinner with wine and cheese", 250)
    Seth.bio()
    


if __name__ == '__main__':
    main()
