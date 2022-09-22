#!/usr/bin/env python
# --------------------------------------------------
# Typing Test
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

import readchar
from pprint import pprint
import argparse
from colorama import Fore, Style
from collections import namedtuple
import random
import time
from datetime import datetime

# namedtuple definition
Input = namedtuple('KeyInput', ['requested', 'received', 'duration'])
UTM = 10

INPUTS = []

def generateCharacter():
    """
    Generates a new random character
    :retturn parameter: character
    """

    # In ASCII the lowercase numbers goes from 97 (a) to 122 (z)
    return chr(random.randint(97, 122))

def runGame(args, start):
    """
    Runs the mini game
    :input parameters: args (type of the game used), start (time the game started)
    """

    count = 0
    hits = 0
    types = 0
    while True:
        # Generate character
        character = generateCharacter()
        print("Type letter: " + Fore.CYAN + character + Style.RESET_ALL)

        # time the user input
        timer = time.time()
        k = readchar.readkey()
        count += 1

        # finish game when the user wants
        if k == " ":
            break

        INPUTS.append(Input(character, k, time.time() - timer))
        types += 1

        if k == character:
            hits += 1

        print("You typed letter: " + (Fore.GREEN if k == character else Fore.RED) + character + Style.RESET_ALL)

        # finish game if time is up or max value has been passed
        if args.use_time_mode == False:
            if count >= args.max_value:
                break
        elif time.time() - start >= UTM:
                break

    return hits, types

def main():

    # Define argparse inputs
    parser = argparse.ArgumentParser(description='Definition of test mode')
    parser.add_argument('-utm','--use_time_mode', action='store_true', help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.', required=False)
    parser.add_argument('-mv','--max_value', type=int, help='Max number of seconds for time mode or maximum number of inputs for number of inputs mode.', required=False)

    # Parse arguments
    args = parser.parse_args()

    if args.use_time_mode == False and args.max_value <= 0:
        print("Inputted Arguments are Invalid!")
        return

    # start the game
    print("To start the game press any key: ")
    start_key = readchar.readchar()

    # time the game
    start = time.time()
    start_tmp = datetime.now().ctime()
    hits, types = runGame(args, start)
    end = time.time()
    end_tmp = datetime.now().ctime()

    # game statistics
    statistics = {
        'accuracy': hits/types,
        'inputs': INPUTS,
        'number_of_hits': hits,
        'number_of_types': types,
        'test_duration': end - start,
        'test_end': end_tmp,
        'test_start': start_tmp,
        'type_average_duration' : (sum([dur.duration for dur in INPUTS]) / len(INPUTS)) if len(INPUTS) > 0 else 0,
        'type_hit_average_duration': (sum([dur.duration for dur in INPUTS if dur.requested == dur.received]) / hits) if hits > 0 else 0,
        'type_miss_average_duration': (sum([dur.duration for dur in INPUTS if dur.requested == dur.received]) / types-hits) if types - hits > 0 else 0
    }

    print()
    pprint(statistics)

if __name__ == '__main__':
    main()