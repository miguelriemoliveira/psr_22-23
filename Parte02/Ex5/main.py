#!/usr/bin/env python
# --------------------------------------------------
# Utilize the readchar package
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

import readchar

def printAllCharsUpTo(stop_char):
    """
    Prints all the characters up to the stop_char character
    :param value: character to stop
    """

    for i in range(ord(stop_char)):
        print(f"{i} - {chr(i)}")

def readAllUpTo(stop_char):
    """
    Reads all the characters in the command line until the stop_char character
    :param value: character to stop
    """

    print("Stopping when you write '" + stop_char + "'")
    while True:
        k = readchar.readkey()
        print(k, end="", flush=True)
        if k == stop_char:
            print()
            break

def countNumbersUpTo(stop_char):
    """
    Counts all the numbers inputted in the command line until the stop_char character
    :param value: character to stop
    """

    lst = []
    nums = []
    others = {}

    while True:
        k = readchar.readkey()
        lst.append(k)
        if k == stop_char:
            break

    total_numbers = 0
    total_others = 0

    print(lst)

    for input in lst:
        if input.isnumeric():
            total_numbers += 1
            nums.append(input)
        else: 
            total_others += 1
            others[total_numbers + total_others] = input


    print('You entered ' + str(total_numbers) + ' numbers.')
    # normal list
    print(nums)
    # sorted list
    print(sorted(nums))
    # list comprehension
    print([x for x in lst if x.isnumeric()])
    print('You entered ' + str(total_others) + ' others.')
    print(others)

def main():
    while True:
        print("\tMENU\n\
            1 - Print All chars up to a character [4.a)]\n\
            2 - Read All chars up to a character [4.b)]\n\
            3 - Count All Numeric numbers up to a character\n\
            4 - Quit")
        option = input("Option: ")
        if option == "1":
            printAllCharsUpTo(readchar.readchar())
        if option == "2":
            readAllUpTo(readchar.readkey())
        if option == "3":
            countNumbersUpTo(readchar.readkey())
        if option == "4":
            break

        

if __name__ == '__main__':
    main()