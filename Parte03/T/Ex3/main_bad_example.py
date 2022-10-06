#!/usr/bin/env python3

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(v1, v2, b3, v4):
    real = b3 + v1
    imaginary = v2 + v4

    # return Complex(real, imaginary)
    return real, imaginary

def multiplyComplex(x, y):
    # (a+bi)(c+di) = ac + adi + bci + bdi2
    a = x.r
    b = x.i
    c = y.r
    d = y.i

    real =  a * c - b* d
    imaginary =  a* d + b * c

    return Complex(real, imaginary)

def printComplex(v1,v2):
    print(str(v1) + '+' + str(v2) + 'i')

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    # A complex number is represented by a named tuple Complex
    # A complex number is a python dictionary with two keys a 'r' and a 'i'
    # A complex number has two value, so I represents them with two variables
    a1 = 5
    a2 = 7
    a3 = 2 
    a4 = 1
    printComplex(a1,a2)
    printComplex(a3,a4)
    
    # Test add
    b1,b2 = addComplex(a1,a2,a3,a4)
    print('Result of addition is:')
    printComplex(b1,b2)

    exit(0)
    # test multiply
    print('Result of multiplication is:')
    printComplex(multiplyComplex(c1, c2))


if __name__ == "__main__":
    main()
