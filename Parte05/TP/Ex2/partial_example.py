#!/usr/bin/python3
import argparse
import functools
import time
import colorama
import cv2

def mysum(a,b):
    return a + b

def mysum_b7(a):
    return mysum(a, 7)

def main():

    # use the function
    print(mysum(4,7))
    print(mysum(3,7))
    print(mysum(9,7))

    mysum_b7 = functools.partial(mysum, b=7)


    print(mysum_b7(9))

if __name__ == '__main__':
    main()
