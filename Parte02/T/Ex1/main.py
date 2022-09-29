#!/usr/bin/env python3

def getDividers(number):
    """Gets the integer dividers of a number
    Args:
        number (int): a number to test
    Returns:
        list: a list of dividers
    """
    
    dividers = []
    for i in range(1,number):    
        # % is the modulus operator which returns the remainder of an integer division
        if number%i == 0: 
            # print(str(i) + ' is an integer divider of ' + str(number))
            dividers.append(i)
            
    # print(str(number) + ' has dividers ' + str(dividers))
    return dividers

def isPerfect(number):
    " Returns True if number is perfect, False otherwise"

    dividers = getDividers(number)

    if sum(dividers) == number:
        return True
    else:
        return False

def main():

    maximum_number = 50  # maximum number to test.

    # write the code ...
    print('Testing for perfect numbers!')

    for number in range(1, maximum_number+1):
        print('Analyzing number ' + str(number))
        if isPerfect(number):
            print(str(number) + ' is perfect!')
        else:
            print(str(number) + ' is not perfect!')
            



if __name__ == '__main__':
    main()


