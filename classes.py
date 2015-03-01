__author__ = 'Valeria'


class Number(object):
    def add(self, summand):
        if (self.imag <> 0) or (summand.imag <> 0):
            new = Complex ()
            new.real = self.real + summand.real
            new.imag = self.imag + summand.imag
            return new.real, new.imag
        else:
            new = Real ()
            new.real = self.real + summand.real
            return new.real

class Integer(Number):
    def __init__(self, real=0):
        self.real = real
        self.imag = 0

class Real(Number):
    def __init__(self, real=0):
        self.real = real
        self.imag = 0

class Complex(Number):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag