__author__ = 'Valeria'

class Animal(object):
    def __init__(self):
        pass
    def eat(self):
        pass
    def whoami(self):
        print 'Animal'

class Mammal(Animal):
    def breath(self):
        pass
    def whoami(self):
        print 'Mammal'

class Winged(Animal):
    def flap(self):
        print 'Flap-flap!'
    def whoami(self):
        print 'Winged'

LittleBat = Mammal()
LittleBat = Winged()

LittleBat.whoami()
# output:NationalGeographic.py
# <class '__main__.Winged'>


# class Bat(Animal, Mammal, Winged):
#     pass
# OUTPUT:
# TypeError: Error when calling the metaclass bases
#    Cannot create a consistent method resolution
# order (MRO) for bases Animal, Mammal, Winged

class Bat(Mammal, Winged):
    pass

NewBat = Bat()
NewBat.whoami()

# OUTPUT:
# Mammal

class Bat(Winged, Mammal):
    pass

NewBat = Bat()
NewBat.whoami()

# OUTPUT:
# Winged

class SuperBat_1 (Bat, Mammal):
    pass

NewBat = SuperBat_1()
NewBat.whoami()

# OUTPUT:
# Winged

class SuperBat_1 (Bat, Winged):
    pass

NewBat = SuperBat_1()
NewBat.whoami()

# OUTPUT:
# Winged

#class SuperBat_1 (Winged, Bat):
#    pass

#NewBat = SuperBat_1()
#NewBat.whoami()

# TypeError: Error when calling the metaclass bases
#     Cannot create a consistent method resolution
# order (MRO) for bases Bat, Winged