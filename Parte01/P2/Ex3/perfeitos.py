#!/usr/bin/python3

from colorama import Fore, Back, Style

maximum_number = 10000

def getDividers(value):
    """
    Outputs a list of dividers d of number value, whose remainder of value/d == 0
    """
    # print('\nReference number ' + str(value))
    dividers = []

    for i in range(1, value):
        remainder = value % i
        # print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            dividers.append(i) # adding element i to the end of the list

    # print('Dividers for reference number '+ str(value) + ' is ' + str(dividers))
    return dividers

def isPerfect(value):

    dividers = getDividers(value)
    sum_of_dividers = sum(dividers)
    if sum_of_dividers == value:
        return True
    else:
        return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print(Fore.RED + Back.YELLOW + Style.DIM + 'Number ' + str(i) + ' is perfect.' + Style.RESET_ALL)

if __name__ == "__main__":
    main()