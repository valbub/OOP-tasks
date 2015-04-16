__author__ = 'Valeria'

class Animal(object):
    def __init__(self):
        pass
    def eat(self):
        pass
    def whoami(self):
        print type(self)

class Mammal(Animal):
    def breath(self):
        pass
    def whoami(self):
        print type(self)

class Winged(Animal):
    def flap(self):
        print 'Flap-flap!'
    def whoami(self):
        print type(self)

Bat = Mammal()
Bat = Winged()

Bat.whoami()
# output:
# <class '__main__.Winged'>

AnotherBat = Winged()
AnotherBat = Mammal()

AnotherBat.whoami()
# output:
# <class '__main__.Mammal'>

AnotherBat = Winged()

AnotherBat.whoami()
# output:
# <class '__main__.Winged'>

Bird = Animal()
Bird = Winged()

Bird.whoami()
# output:
# <class '__main__.Winged'>

AnotherBird = Winged()
AnotherBird = Animal()

AnotherBird.whoami()
# output:
# <class '__main__.Animal'>

# AnotherBird.flap()
# output:
# AttributeError: 'Animal' object has no attribute 'flap'