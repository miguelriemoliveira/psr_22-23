
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

