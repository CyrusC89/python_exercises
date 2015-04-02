#!/usr/bin/env python
class Vehicle:
    wheels = 4
    color = "white"
    seats = 2
    flying = False

class Aerial_Vehicle(Vehicle):
    flying = True
    def fly(self):
        print "We are flying all over the fucking place in our %s" % self.name

class Car(Vehicle):
    def __init__(self):
        self.seats = 5
    def horn(self):
        print "meep meep"

class Helicopter(Aerial_Vehicle):
    flying = True
    def __init__(self, name="helicopter", heli_type="commanche"):
        self.name = name
        self.heli_type = heli_type

class Van(Car):
    def __init__(self, color, brand):
        self.seats = 13
        self.color = color
        self.brand = brand


my_van = Van("Red", "Chevy")

my_car = Car()
my_car.horn()
apache = Helicopter(heli_type="apache")
apache.fly()
