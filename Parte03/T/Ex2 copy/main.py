#!/usr/bin/env python3

def addComplex(x, y):
    # (a+bi) + (c+di) = (a+c) + (b+d)i     

    # alternative 1
    a, b = x
    c, d = y

    real = a + c
    imaginary = b + d

    # alternative 2
    # real = x[0] + y[0]
    # imaginary = x[1] + y[1]

    return (real, imaginary)

def multiplyComplex(x, y):
    # (a+bi)(c+di) = ac + adi + bci + bdi2
    a, b = x
    c, d = y

    real =  a * c - b* d
    imaginary =  a* d + b * c

    return (real, imaginary)

def printComplex(x):
    real, imaginary = x
    print(str(real) + '+' + str(imaginary) + 'i')

def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    # A complex number is represented as a tuple (real, imaginary)
    c1 = (5, 3)
    c2 = (-2, 7)
    printComplex(c1)
    printComplex(c2)
    

    # Test add
    c3 = addComplex(c1, c2)
    print('Result of addition is:')
    printComplex(c3)

    # test multiply
    print('Result of multiplication is:')
    printComplex(multiplyComplex(c1, c2))


if __name__ == "__main__":
    main()
