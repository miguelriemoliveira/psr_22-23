#!/usr/bin/python3

from colorama import Fore, Back, Style

maximum_number = 155


def isPrime(value):

    print('\nAnalisyng number ' + str(value))

    for i in range(2, value): # visit all numbers between 1 and value, exluding those two.
        remainder = value % i
        print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            return False

    return True


def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    count = 0 # initialize the counter
    for i in range(1, maximum_number):
        if isPrime(i):
            print('Number ' + Fore.YELLOW + Back.GREEN + str(i) + Style.RESET_ALL + ' is prime.' )
            count = count + 1
        else:
            print('Number ' + str(i) + ' is not prime.')

    print(Fore.BLUE  + 'I found ' + str(count) + ' prime numbers between 1 and ' + str(maximum_number) + Style.RESET_ALL)


if __name__ == "__main__":
    main()
