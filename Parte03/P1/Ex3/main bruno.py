#!/usr/bin/env python3
from colorama import Fore, Style, Back


def myFunction(a1, a2=7, a3=4):
    print('a1 = ' + str(a1))
    print('a2 = ' + str(a2))
    print('a3 = ' + str(a3))
    return True


def main():

    myFunction(1,2,3)

    myFunction(a1=1, a2=2, a3=3)

    myFunction(a3=3, a2=2, a1=1)
    
    myFunction(1,2,a3=3)

    # myFunction(a3=3, 1 ,2)

    myFunction(1)

    myFunction(a3=3, a1=1)

    myFunction(1, a3=3)


    
if __name__ == "__main__":
    main()

