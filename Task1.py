__author__ = 'Valeria'

class Integer(object):
    def __init__(self, number):
        self.module = number
    def add (self, summand):
        if isinstance(summand, Integer):
            new = Integer
            new.module = self.module + summand.module
            return new.module
        else:
            raise Exception( 'Error: different types.' )

class Rational(object):
    def __init__(self, number):
        self.module = number
    def add(self, summand):
        if isinstance (summand, Rational):
            new = Rational
            new.module = self.module + summand.module
            return new.module
        else:
            raise Exception( 'Error: different types.' )

class Complex(object):
    def __init__(self, realpart=None, imagpart =None):
        self.imaginary = imagpart
        self.real = realpart
#    def getreal(self):
#        return self.real
#    def setreal(self, value):
#        self.real = value
#    real = property(getreal, setreal, "Property of real")
    def add(self, summand):
        if isinstance (summand, Complex):
            new = Complex()
            new.real = self.real + summand.real
            new.imaginary = self.imaginary + summand.imaginary
            return (new.real, new.imaginary)
        else:
            raise Exception( 'Error: different types.' )


x1 = Complex(1, -4)
y1 = Complex(7, 2)

x2 = Rational(5.25)
y2 = Rational(20.17)

x3 = Integer(6)
y3 = Integer(15)


def sum(a, b):
   return a.add(b)

print sum (x1, y1)
print sum (x2, y2)
print sum (x3, y3)