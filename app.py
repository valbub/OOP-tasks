__author__ = 'Valeria'

from classes import *

ex1 = Complex(1.15, 6)
ex2 = Real(2.67)
ex3 = Real(1.15)
ex4 = Quaternion(2, 5.32, 5, 8.98)
ex5 = Quaternion(24, 62, 3, 8)

def sum(a, b):
   return a.add(b)

res = sum(ex4, ex5)

print res, type(res)

'''Result from
      return '%s'% self.__dict__:
{'real': 26, 'imaginary': 67.32, 'jcomponent': 8, 'kcomponent': 16.98} <class 'classes.Quaternion'>'''