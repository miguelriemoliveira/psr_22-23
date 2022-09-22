#!/usr/bin/env python3
###!/usr/bin/python3 # versão manual

# Imports
from colorama import Fore, Back, Style

# Global variable
maximum_number = 10


# This is a function to assert if number value is a prime or not.
# If the value is prime, return True, else return False.
def isPrime(value):
    
    for number in range(2, value):
        remainder = value % number
        print(str(value) + '/' + str(number) + ' = '+  str(remainder))
        if remainder == 0: # I am sure number is not prime
            return False 

    # if I get here then there was no divider with remainder zero
    return True

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for number in range(1, maximum_number + 1):
        if isPrime(number):
            print(Style.BRIGHT + Back.YELLOW +  Fore.GREEN + 'Number ' + str(number) + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(number) + ' is not prime.')

if __name__ == "__main__":
    main()
