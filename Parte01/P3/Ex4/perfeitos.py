#!/usr/bin/python3

from colorama import Fore, Back, Style

maximum_number = 7

def getDividers(value):
    dividers = [1]

    for i in range(2, value):  # visit all numbers between 1 and value, exluding those two.
        remainder = value % i
        # print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            dividers.append(i)

    print('dividers of number ' + str(value)  + '= ' + str(dividers))
    return dividers

def isPrime(value):

    print('\nAnalisyng number ' + str(value) + ' to see if its prime')

    dividers = getDividers(value)

    if len(dividers) > 1:
        return False
    else:
        return True

def isPerfect(value):
    print('\nAnalisyng number ' + str(value) + ' to see if its perfect')

    dividers = getDividers(value)

    if sum(dividers) == value:
        return True  # the number value is perfect
    else:
        return False


def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')
        if isPrime(i):
                print('Number ' + str(i) + ' is prime.')


if __name__ == "__main__":
    main()
