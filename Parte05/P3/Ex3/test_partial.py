#!/usr/bin/python3
import argparse
import copy
import functools
import time
import colorama
import cv2
import numpy as np

def myAddition(a, b):
    return a + b

def myAdd7(x):
    return x + 7

def main():

    # call myAddition
    print(myAddition(3,7))
    print(myAddition(1,7))
    print(myAddition(8,7))

    print(myAdd7(3))

    myAdd7_with_partial = functools.partial(myAddition, b=7)

    print(myAdd7_with_partial(3))

if __name__ == '__main__':
    main()
