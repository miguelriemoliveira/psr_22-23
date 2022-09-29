#!/usr/bin/env python3

import argparse  # import argparse library


def soma(p1,p2, verbose=False):
    total = p1 + p2
    if verbose:
        print('Eu calculei o total cá dentro !!! ')
    return  total

def main():

    # maximum_number = 2  # maximum number to test.

    parser = argparse.ArgumentParser(description='Test for PSR.')
    parser.add_argument('-p1', '--parcela1', type=int, required=False, default=5)
    parser.add_argument('-p2', '--parcela2', type=int, required=False, default=4)

    args = vars(parser.parse_args())
    print(args)
           
    p1 = args['parcela1']
    p2 = args['parcela2']
    total = soma(p1,p2)
    total = soma(p1,p2)
    total = soma(p1,p2, verbose=True)

    print('parcela 1 = ' + str(p1))
    print('parcela 2 = ' + str(p2))

    print('soma = ' +str(total))



if __name__ == '__main__':
    main()


