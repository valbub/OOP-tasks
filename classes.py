__author__ = 'Valeria'


class Number(object):
    def __str__(self):
#        return '%s'% self.__dict__
        a = ''
        for key in sorted(self.__dict__):
            Component = key[-1:]
            a += str(self.__dict__[key]) + Component + ' '
        return a

class Real(Number):
    def __init__(self, real=0):
        self.Component__r = real
        self.Component_i = 0
    def add(self, summand):
        new = Real()
        new.Component__r = self.Component__r + summand.Component__r
        return new

class Complex(Real):
    def __init__(self, real=0, imag=0):
        super(Complex, self).__init__(real)
        self.Component_i = imag
    def add(self, summand):
        new = Complex()
        new.Component__r = self.Component__r + summand.Component__r
        try:
            new.Component_i = self.Component_i + summand.Component_i
        except AttributeError:
            new.Component_i = self.Component_i
        return new

class Quaternion(Complex):
    def __init__(self, real=0, imag=0, jcomp=0, kcomp=0):
        super(Quaternion, self).__init__(real, imag)
        self.Component_j = jcomp
        self.Component_k = kcomp
    def add(self, summand):
        new = Quaternion()
        new.Component__r = self.Component__r + summand.Component__r
        new.Component_i = self.Component_i + summand.Component_i
        try:
            new.Component_j = self.Component_j + summand.Component_j
        except AttributeError:
            new.Component_j = self.Component_j
        try:
            new.Component_k = self.Component_k + summand.Component_k
        except AttributeError:
            new.Component_k = self.Component_k
        return new