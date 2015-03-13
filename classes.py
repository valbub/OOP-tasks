__author__ = 'Valeria'


class Number(object):
    pass

class Integer(Number):
    def __init__(self, real=0):
        self.real = real
        self.imaginary = 0
    def add(self, summand):
        new = Real()
        new.real = self.real + summand.real
        return new
    def __str__(self):
        return '%s' % self.real

class Real(Integer):
    def __init__(self, real=0):
        super(Real, self).__init__(real)
        self.real = real

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
    def __str__(self):
      return '%s %s' % (self.real, self.imaginary)

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
    def __str__(self):
      return '%s %si %sj %sk' % (self.real, self.imaginary, self.jcomponent, self.kcomponent)