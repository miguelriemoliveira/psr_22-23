#!/usr/bin/env python3
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# --------------------------------------------------
from copy import deepcopy
from functools import partial

import numpy as np
import cv2
from colorama import Fore, Style


def somar(p1, p2):
    return p1 + p2

# def somar777(p1):
#     return somar(p1, 777)
# 


def main():
    a = 1
    b = 2
    c = somar(a,b)

    somar777 = partial(somar, p2=777)

    for n in range(0, 5):
        # print('n=' + str(n) + ' +  777 = ' + str(somar(n,777) ))
        print('n=' + str(n) + ' +  777 = ' + str(somar777(n) ))


if __name__ == '__main__':
    main()
