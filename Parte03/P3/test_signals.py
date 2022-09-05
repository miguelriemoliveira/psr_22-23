#!/usr/bin/python3
import random
import signal
import sys
import time

from colorama import Fore, Back, Style
import pyautogui
import readchar


def timeout_callback(num, stack):
    # print("Received SIGALRM " + str(num))
    # print("Aborting the program ... computing the current statistics")
    raise ValueError("Time available for input ended")
    # sys.exit(0)
    # raise Exception("FUBAR")

def main():

    # signal.alarm(3)
    # signal.signal(signal.SIGALRM, timeout_callback)
    #
    # # Create a complex number as an instance of class ComplexClass
    # print('Type something ... I only give you 3 secs ...')
    #
    # try:
    #     k = readchar.readchar()
    # except:
    #
    #     pyautogui.press("t")
    #     print("\nPressed t")
    #     print("An exception occurred")

    d = dict(Fore.__dict__.items())

    colors = []
    for k in d.keys():
        colors.append(d[k])

    print(colors)
    # colors = [Fore.RED, Fore.BLUE, Fore.MAGENTA, Fore.GREEN]
    while True:
        n = random.randint(0, 100)
        color = random.choice(colors)
        print(color + "number is " + str(n) , end="\r" )
        time.sleep(0.1)

    print(Style.RESET_ALL)
if __name__ == '__main__':
    main()
