__author__ = 'Valeria'


class Number(object):
    def __str__(self):
#        return '%s'% self.__dict__
        a = ''
        for i in range(len(self.__dict__.keys())):
            if self.__dict__.keys()[i] == 'real':
                a += str(self.__dict__[(self.__dict__.keys())[i]]) + ' '
            else:
                a += str(self.__dict__[(self.__dict__.keys())[i]]) + str(self.__dict__.keys()[i]) + ' '
        return a

class Real(Number):
    def __init__(self, real=0):
        self.real = real
        self.i = 0
    def add(self, summand):
        new = Real()
        new.real = self.real + summand.real
        return new

class Complex(Real):
    def __init__(self, real=0, imag=0):
        super(Complex, self).__init__(real)
        self.i = imag
    def add(self, summand):
        new = Complex()
        new.real = self.real + summand.real
        try:
            new.i = self.i + summand.i
        except AttributeError:
            new.i = self.i
        return new

class Quaternion(Complex):
    def __init__(self, real=0, imag=0, jcomp=0, kcomp=0):
        super(Quaternion, self).__init__(real, imag)
        self.j = jcomp
        self.k = kcomp
    def add(self, summand):
        new = Quaternion()
        new.real = self.real + summand.real
        new.i = self.i + summand.i
        try:
            new.j = self.j + summand.j
        except AttributeError:
            new.j = self.j
        try:
            new.k = self.k + summand.k
        except AttributeError:
            new.k = self.k
        return new