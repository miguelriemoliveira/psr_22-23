maximum_number = 10000


def isPrime(x):

    for divider in range(2, x):
        remainder = x % divider
        # print(str(x) + '/' + str(divider) + ' tem resto ' + str(remainder))

        if remainder == 0:
            # print('This number is not prime')
            return False

    return True

def main():
    # import os
    # os.system('cls' if os.name == 'nt' else 'clear')
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(1, maximum_number + 1):
        if isPrime(i):
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

if __name__ == "__main__":
    main()
