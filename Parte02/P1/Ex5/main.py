#!/usr/bin/env python3

import argparse  # import argparse library

from readchar import readkey, key


def countNumbersUpTo(stop_char):

    inputs = []
    while True: # get the inputs
        k = readkey()
        print('You entered ' + k)

        if k == stop_char:
            break

        inputs.append(k)


    # Process the inputs to figure out how many numeric inputs there were
    numeric_inputs = [x for x in inputs if x.isnumeric()]
    other_inputs = [x for x in inputs if not x.isnumeric()]
    other_inputs2 = [x for x in inputs if not x in numeric_inputs] # ???

    print('numeric_inputs: ' + str(numeric_inputs))
    print('other_inputs: ' + str(other_inputs))
    print('other_inputs2: ' + str(other_inputs2))

    # Ex5c
    
    # other_inputs_dict = {}
    # count = 0
    # for other_input in other_inputs2:
    #     other_inputs_dict[count] = other_input
    #     count += 1
    #     
#     other_inputs_dict = {}
#     count = 0
#     for input in inputs:
#         if input.isnumeric():
#             other_inputs_dict[count] = input
#         count += 1
# 

    other_inputs_dict = {}
    for other_input in other_inputs2:
        key = inputs.index(other_input)
        other_inputs_dict[key] = other_input


        

    print('other_inputs_dict = ' + str(other_inputs_dict))
#     total_numbers = 0
#     total_others = 0
    # print('You entered ' + str(total_numbers) + ' numbers.')
    # print('You entered ' + str(total_others) + ' others.')

def main():

    # maximum_number = 2  # maximum number to test.

    parser = argparse.ArgumentParser(description='Test for PSR.')
    parser.add_argument('-sc', '--stop_char', type=str, required=False, default='x')

    args = vars(parser.parse_args())
           
    countNumbersUpTo(args['stop_char'])

if __name__ == '__main__':
    main()


