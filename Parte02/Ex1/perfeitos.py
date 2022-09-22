#!/usr/bin/env python
# --------------------------------------------------
# Calculate perfect numbers
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------


maximum_number = 100

def getDividers(value):
    """
    Return a list of dividers for the number value
    :param value: the number to test
    :return: a list of dividers.
    """

    divisors = [1]

    for i in range(2, int(value / 2) + 1):
        if value % i == 0:
            divisors.append(i)
            divisors.append(value/i)

    return divisors


def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """

    if value == 0 or value == 1:
        return False

    divisors = getDividers(value)

    if sum(list(set(divisors))) == value:
        return True

    return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()