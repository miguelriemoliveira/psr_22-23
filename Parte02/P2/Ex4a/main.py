#!/usr/bin/env python3

from readchar import readkey


def readCharsUpTo(stop_char):

    while True: 
        print('Enter a key')
        key = readkey()

        print('You pressed ' + key)

        if key == stop_char:
            break

def printAllPreviousChars():

    stop_character = readkey()
    stop_number = ord(stop_character)

    print('Printing all chars up to ' + stop_character)

    characters = []
    for number in range(32, stop_number):
        character = chr(number)
        characters.append(character)
        # print(character + str('\n'))

    print(characters)

# def countNumbersUpTo(stop_char):
# 
#     # 1. Read all the inputs and see if they are numeric and then count them
#     total_numbers = 0
#     total_others = 0
#     while True: 
#         print('Enter a key')
#         key = readkey()
#         print('You pressed ' + key)
# 
#         if key == stop_char:
#             break
# 
#         if key.isnumeric():
#             total_numbers += 1
#         else:
#             total_others += 1
#     
#     print('You entered ' + str(total_numbers) + ' numbers.')
#     print('You entered ' + str(total_others) + ' others.')
# 

def countNumbersUpTo(stop_char):

    # 1. Read all the inputs and put them in the keys list
    keys = []
    while True: 
        print('Enter a key')
        key = readkey()
        print('You pressed ' + key)

        if key == stop_char:
            break

        keys.append(key)

    print('User pressed ' + str(keys))

    # 2. Process the list of keys and figure out which of those are numbers
    keys_numbers =[]
    keys_others=[] 
    for key in keys:
        if key.isnumeric():
            keys_numbers.append(key)
        else:
            keys_others.append(key)
    
    print('Keys numbers ' + str(keys_numbers))
    print('Keys others ' + str(keys_others))

    total_numbers = len(keys_numbers)
    total_others = len(keys_others)
 
    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')


    # Create the dictionary Ex5c
    keys_dict = {}
    counter = 0
    for key in keys:
        if key.isnumeric():
            keys_dict[counter] = key

        counter += 1

    print(keys_dict)

def main():

    # Ex4a
    # printAllPreviousChars()
    
    #Ex4b
    # readCharsUpTo('x')

    #Ex4c
    countNumbersUpTo('x')

if __name__ == "__main__":
    main()
