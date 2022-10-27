#!/usr/bin/env python3
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# --------------------------------------------------
from copy import deepcopy
from functools import partial
from re import I
from tkinter import W

import numpy as np
import cv2
from colorama import Fore, Style

# GLOBAL VARIABLES ARE FORBIDDEN

def showBoolImage(win_name, image):
    image_bool = image.astype(np.uint8)*255
    cv2.imshow(win_name, image_bool)

def main():
    # initial setup
    image = cv2.imread('./atlascar.png')
    cv2.namedWindow( 'rgb_image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('rgb_image', 800, 400)


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,t_image = cv2.threshold(gray,230,255,cv2.THRESH_BINARY)

    connectivity = 4  # You need to choose 4 or 8 for connectivity type
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(t_image , connectivity , cv2.CV_32S)
    print('num_labels = ' + str(num_labels))
    print('stats = ' + str(stats))
    print('centroids = ' + str(centroids))
    
    # find the second larges object (fisrt one is the background)
    largest_area_idx = None
    largest_area = 0
    for idx, stat in enumerate(stats):
        if idx == 0:
            continue
        print(stat)
        print(cv2.CC_STAT_AREA)
        area = stat[cv2.CC_STAT_AREA]

        if area > largest_area:
            largest_area = area
            largest_area_idx = idx

    print('Component with largest area is idx = ' + str(largest_area_idx) + ' with area = ' + str(largest_area))
    xc =centroids[largest_area_idx][0]
    yc =centroids[largest_area_idx][1]

    print('Component with largest area is idx = ' + str(largest_area_idx) + ' with area = ' + str(largest_area), ' , centroid x=' + str(xc) + ', yc= ' + str(yc))

    cv2.imshow('rgb_image', image)
    cv2.imshow('thresholded_image', t_image)


    pressed_key = cv2.waitKey(0)

if __name__ == '__main__':
    main()
