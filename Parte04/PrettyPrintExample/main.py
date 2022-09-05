#!/usr/bin/python3
import argparse
import json
import pprint

def main():

    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('-utm', '--use_time_mode', action='store_true', help='')
    parser.add_argument('-mn', '--max_number', type=int, help='')
    args = vars(parser.parse_args())
    print(args)

    if args['use_time_mode']:
        print('Using time mode. test will run up to ' + str(args['max_number']) + ' seconds')
    else:
        print('Not using time mode. Test will ask for ' + str(args['max_number']) + ' responses')



if __name__ == '__main__':
    main()
