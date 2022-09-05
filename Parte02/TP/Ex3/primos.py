#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse


def isPrime(value):

    print('\nAnalisyng number ' + str(value))

    for i in range(2, value): # visit all numbers between 1 and value, exluding those two.
        remainder = value % i
        print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            return False

    return True


def main():

    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('--maximum_number', type=int, help='Maximum number to search for primes.')
    parser.add_argument('--verbose', action='store_true', help='print stuff to the screen or not.')
    args = vars(parser.parse_args())
    print(args)

    print("Starting to compute prime numbers up to " + str(args['maximum_number']))
    count = 0 # initialize the counter
    for i in range(1, args['maximum_number']):
        if isPrime(i):
            print('Number ' + Fore.YELLOW + Back.GREEN + str(i) + Style.RESET_ALL + ' is prime.' )
            count = count + 1
        else:
            print('Number ' + str(i) + ' is not prime.')

    if args['verbose']:
        print(Fore.BLUE  + 'I found ' + str(count) + ' prime numbers between 1 and ' + str(args['maximum_number']) + Style.RESET_ALL)


if __name__ == "__main__":
    main()
