#!/usr/bin/env python3
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# --------------------------------------------------
from copy import deepcopy

import numpy as np
import cv2
from colorama import Fore, Style

is_drawing = False
gui_image = None
xs = []
ys = []
pencil_color = (0,255,0)
# partial functionality

def mouseCallback(event, x, y, flags, userdata):
    global is_drawing, gui_image, pencil_color

    # print('Mouse event at x=' + str(x) + ' y=' + str(y))


    if event == cv2.EVENT_LBUTTONDOWN:
        if is_drawing:
            print('Stop drawing')
            is_drawing = False
        else:
            print('Start drawing')
            is_drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if is_drawing:
            xs.append(x)
            ys.append(y)
            
            for xi, yi in zip(xs, ys): # iterating all the stored coordinates and drawing a points for each
                cv2.line(gui_image, (xi, yi), (xi, yi), (255,0,0), 2)

            if len(xs) > 2:
                # for idx in range(0, len(xs)-1):
                idxs = list(range(0, len(xs)))
                for idx1, idx2 in zip(idxs[:-1], idxs[1:]):
                    x1 = xs[idx1]
                    y1 = ys[idx1]
                    x2 = xs[idx2]
                    y2 = ys[idx2]
                    cv2.line(gui_image, (x1, y1), (x2, y2), (0,200,0), 1)


def main():
    # initial setup
    global gui_image, xs, ys
    image = cv2.imread('../images/atlascar.png')
    gui_image = deepcopy(image)
    window_name = 'Window'
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    cv2.setMouseCallback(window_name, mouseCallback)

    while True:
        cv2.imshow(window_name, gui_image)
        pressed_key = cv2.waitKey(30)

        if pressed_key == -1:
            pass
        elif chr(pressed_key) == 'q': # Quite the program
            exit(0)
        elif chr(pressed_key) == 'c': # Clear the drawing
            print(Fore.RED + 'You pressed c' + Style.RESET_ALL)
            xs = []
            ys = []
            gui_image = deepcopy(image)


if __name__ == '__main__':
    main()
