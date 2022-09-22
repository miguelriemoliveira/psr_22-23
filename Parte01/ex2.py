#!python

from colorama import Fore, Style

maximum_number = 50

def isPrime(value):
    if value == 0:
        return 0

    for i in range(2, int(value / 2) + 1):
        if value % i == 0:
            print(f"Divisores: {sorted(list(set([1, i, int(value/i), value])))}")
            return 0
    return 1

def main():
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        print()
        if isPrime(i):
            print('Number ' + Fore.GREEN + str(i) + Style.RESET_ALL + ' is prime.')
        else:
            print('Number ' + Fore.GREEN + str(i) + Style.RESET_ALL + ' is not prime.')

if __name__ == "__main__":
    main()