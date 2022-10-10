#!/usr/bin/env python
# --------------------------------------------------
# Complex Numbers with named tuples
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(x, y):
    return Complex(x.r + y.r, x.i + y.i)

def multiplyComplex(x, y):
    result_real = x.r * y.r - x.i * y.i
    result_im = x.r * y.i + x.i * y.r
    return Complex(result_real, result_im)

def printComplex(x):
    print(str(x.r) + ' + ' + (str(x.i) + 'i' if x.i != 0 else ""))


def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1)) # named tuple looks nice when printed

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()