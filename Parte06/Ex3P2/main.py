#!/usr/bin/env python3
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# --------------------------------------------------
from copy import deepcopy
from functools import partial

import numpy as np
import cv2
from colorama import Fore, Style

# GLOBAL VARIABLES ARE FORBIDDEN

def mouseCallback(event, x, y, flags, userdata, options):

    if event == cv2.EVENT_LBUTTONDOWN:
        if options['is_drawing']:
            print('Stop drawing')
            options['is_drawing'] = False
        else:
            print('Start drawing')
            options['is_drawing'] = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if options['is_drawing']:
            options['xs'].append(x)
            options['ys'].append(y)
            
            if len(options['xs']) > 2:
                x1 = options['xs'][-2]
                y1 = options['ys'][-2]
                x2 = options['xs'][-1]
                y2 = options['ys'][-1]
                cv2.line(options['gui_image'], (x1, y1), (x2, y2), options['pencil_color'], 1)


def main():
    # initial setup
    image = cv2.imread('../images/atlascar.png')
    window_name = 'Window'
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 400)

    options = {'is_drawing' : False,'gui_image' : deepcopy(image),
               'xs' : [], 'ys' : [],'pencil_color' : (0,255,0)}

    cv2.setMouseCallback(window_name, partial(mouseCallback, options=options))

    while True:
        cv2.imshow(window_name, options['gui_image'])
        pressed_key = cv2.waitKey(30)

        if pressed_key == -1:
            pass
        elif chr(pressed_key) == 'q': # Quite the program
            exit(0)
        elif chr(pressed_key) == 'c': # Clear the drawing
            print(Fore.RED + 'You pressed c' + Style.RESET_ALL)
            options['xs'] = []
            options['ys'] = []
            options['gui_image'] = deepcopy(image)
        elif chr(pressed_key) == 'r': # Pencil color red
            options['pencil_color'] = (0,0,255)
            



if __name__ == '__main__':
    main()
