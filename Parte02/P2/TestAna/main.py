#!/usr/bin/env python3

from readchar import readkey


def readCharsUpTo(stop_char):

    while True: 
        print('Enter a key')
        key = readkey()

        print('You pressed ' + key)

        if key == stop_char:
            break


def main():
    print('Hello')
    readCharsUpTo('x')

if __name__ == "__main__":
    main()
