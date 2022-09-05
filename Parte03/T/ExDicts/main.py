#!/usr/bin/python3
import colorama

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    a = x['r']
    b = x['i']
    c = y['r']
    d = y['i']
    return {'r': a + c, 'i': b + d}


def main():
    cs = {'c1': {'r': 4, 'i': 8}, 'c2': {'r': 8, 'i': -4}}

    print(cs['c1'])
    print(cs['c2'])
    cs['c3'] = addComplex(cs['c1'], cs['c2'])

    print(cs)


if __name__ == '__main__':
    main()
