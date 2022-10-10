#!/usr/bin/env python
# --------------------------------------------------
# Complex Numbers with tuples
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

def addComplex(x, y):
    return (x[0] + y[0], x[1] + y[1])

def multiplyComplex(x, y):
    result_real = x[0] * y[0] - x[1] * y[1]
    result_im = x[0] * y[1] + x[1] * y[0]
    return (result_real, result_im)

def printComplex(x):
    print(str(x[0]) + ' + ' + (str(x[1]) + 'i' if x[1] != 0 else ""))


def main():
    # ex2 a)

    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()