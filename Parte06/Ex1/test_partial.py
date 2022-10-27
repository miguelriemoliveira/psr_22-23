#!/usr/bin/env python3
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# --------------------------------------------------
import random
import string
from copy import deepcopy
from functools import partial
from sys import prefix
from tkinter.ttk import Separator

import numpy as np
import cv2
from colorama import Fore, Style


def textAddOn(text,  suffix,  prefix):
    separator = '-'
    return prefix + separator + text + separator + suffix

# def textAddOnDr(text, suffix, separator='-'):
#     return textAddOn(text=text, prefix='Dr', suffix=suffix, separator=separator)


def main():

    print(textAddOn('Manuel', 'Dr', 'NO LAST NAME'))
    name = 'Oliveira'


    textAddOnDr = partial(textAddOn, prefix='Dr')

    for i in range(0,5):
        letters = string.ascii_lowercase
        name = ''.join(random.choice(letters) for i in range(10)) 
        # print(textAddOn(name , 'Dr', name))    

        print(textAddOnDr(name , name))    


        


if __name__ == '__main__':
    main()
