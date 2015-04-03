__author__ = 'Valeria'


class Number(object):
    def __str__(self):
#        return '%s'% self.__dict__
        a = ''
        for i in range(len(self.__dict__.keys())):
            a += str(self.__dict__[(self.__dict__.keys())[i]]) + ' '
        return a

class Real(Number):
    def __init__(self, real=0):
        self.real = real
        self.imaginary = 0
    def add(self, summand):
        new = Real()
        new.real = self.real + summand.real
        return new

class Complex(Real):
    def __init__(self, real=0, imag=0):
        super(Complex, self).__init__(real)
        self.imaginary = imag
    def add(self, summand):
        new = Complex()
        new.real = self.real + summand.real
        try:
            new.imaginary = self.imaginary + summand.imag
        except AttributeError:
            new.imaginary = self.imaginary
        return new

class Quaternion(Complex):
    def __init__(self, real=0, imag=0, jcomp=0, kcomp=0):
        super(Quaternion, self).__init__(real, imag)
        self.jcomponent = jcomp
        self.kcomponent = kcomp
    def add(self, summand):
        new = Quaternion()
        new.real = self.real + summand.real
        new.imaginary = self.imaginary + summand.imaginary
        try:
            new.jcomponent = self.jcomponent + summand.jcomponent
        except AttributeError:
            new.jcomponent = self.jcomponent
        try:
            new.kcomponent = self.kcomponent + summand.kcomponent
        except AttributeError:
            new.kcomponent = self.kcomponent
        return new