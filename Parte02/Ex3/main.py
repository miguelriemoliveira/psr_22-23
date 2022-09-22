#!/usr/bin/env python
# --------------------------------------------------
# Calculate prime numbers
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

# Imports
from colorama import Fore, Back, Style
from my_functions import isPrime

def main():

    maximum_number = int(input("Max Limit: "))

    print("Starting to compute prime numbers up to " + str(maximum_number))

    for number in range(1, maximum_number + 1):
        if isPrime(number):
            print(Style.BRIGHT + Back.YELLOW +  Fore.GREEN + 'Number ' + str(number) + ' is prime.' + Style.RESET_ALL)
        else:
            print('Number ' + str(number) + ' is not prime.')

if __name__ == "__main__":
    main()
