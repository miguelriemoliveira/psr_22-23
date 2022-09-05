#!/usr/bin/python3
import time

import colorama

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    a = x.r
    b = x.i
    c = y.r
    d = y.i
    return Complex(r=a + c, i=b + d)


def multiplyComplex(x, y):
    a = x.r
    b = x.i
    c = y.r
    d = y.i
    result_real = a * c - b * d
    result_im = a * d + b * c
    return Complex(result_real, result_im)


def printComplex(x, prefix=''):
    a = x.r
    b = x.i
    print(prefix + str(a) + '+' + str(b) + 'i')

def addTwo(self, x, y):
    a = x.r
    b = x.i
    c = y.r
    d = y.i
    return ComplexClass(r=a + c, i=b + d)

class ComplexClass:
    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, x):
        a = self.r
        b = self.i
        c = x.r
        d = x.i
        self.r = a + c
        self.i = b + d

    def multiply(self, x):
        a = self.r
        b = self.i
        c = x.r
        d = x.i
        self.r = a * c - b * d
        self.i = a * d + b * c

    def __str__(self):
        a = self.r
        b = self.i
        return str(a) + '+' + str(b) + 'i'


def main():
    # Create a complex number as an instance of class ComplexClass

    c1 = ComplexClass(4, 8)
    print('c1')
    print(c1)
    c2 = ComplexClass(6, -7)
    print('c2')
    print(c2)

    print('Doing nothing for 30secs ...')
    time.sleep(300)
    # c3 = addTwo(c2, c2)

    # print('c3')
    # print(c3)
    # c1.add(c2)
    # print(c1)
    # c1.multiply(c2)
    # print(c1)


if __name__ == '__main__':
    main()
