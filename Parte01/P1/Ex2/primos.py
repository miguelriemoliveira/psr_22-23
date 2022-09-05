#!/usr/bin/python3

from colorama import Fore, Back, Style

maximum_number = 101


def isPrime(value):
   print('\nChecking if ' + str(value) + ' is prime:')

   for i in range(2,value):
      remainder = value % i
      print('Division by ' + str(i) + ' is ' + str(remainder))
      if remainder == 0:
         print(str(value) + ' is not prime because division by ' + str(i) + ' has 0 remainder')
         return False

   return True

def main():
   print("Starting to compute prime numbers up to " + str(maximum_number - 1))

   count = 0
   for i in range(1, maximum_number):
      if isPrime(i):
         count += 1
         print(Fore.RED + Back.YELLOW + Style.BRIGHT +  'Number ' + Fore.LIGHTYELLOW_EX + Back.GREEN + Style.BRIGHT
               + str(i) + Fore.RED + Back.YELLOW + Style.BRIGHT + ' is prime.' + Style.RESET_ALL )
      else:
         print('Number ' + str(i) + ' is not prime.')
         pass


   print(Fore.BLUE + 'Between 1 and ' + str(maximum_number) + ' there are ' + str(count) +
         ' prime numbers' + Style.RESET_ALL)

if __name__ == "__main__":
    main()