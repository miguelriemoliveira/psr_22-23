#!/usr/bin/env python
# --------------------------------------------------
# OpenCV TrackBar
# Filipe Gonçalves, 98083
# PSR, Setember 2022.
# --------------------------------------------------

import argparse
import cv2
import numpy as np
import copy
from functools import partial
import json

def onTrackbar(value, channel, min_max, window_name, ranges, image):
    ranges[channel][min_max] = value  # update corresponding value in ranges dict

    # Processing
    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(image, mins, maxs)
    mask = mask.astype(bool)  # conversion from numpy from uint8 to bool

    image_processed = copy.deepcopy(image)
    image_processed[np.logical_not(mask)] = 0
    cv2.imshow(window_name, image_processed)


def main():

    window_name = 'window - Ex3a'

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    ranges = {'b': {'min': 0, 'max': 256},
              'g': {'min': 0, 'max': 256},
              'r': {'min': 0, 'max': 256}}

    # add code to create the trackbar ...
    cv2.createTrackbar('MinB', window_name, 0,   256, partial(onTrackbar, channel='b', min_max='min',window_name=window_name, image=image, ranges=ranges))
    cv2.createTrackbar('MaxB', window_name, 256, 256, partial(onTrackbar, channel='b', min_max='max',window_name=window_name, image=image, ranges=ranges))
    cv2.createTrackbar('MinG', window_name, 0,   256, partial(onTrackbar, channel='g', min_max='min',window_name=window_name, image=image, ranges=ranges))
    cv2.createTrackbar('MaxG', window_name, 256, 256, partial(onTrackbar, channel='g', min_max='max',window_name=window_name, image=image, ranges=ranges))
    cv2.createTrackbar('MinR', window_name, 0,   256, partial(onTrackbar, channel='r', min_max='min',window_name=window_name, image=image, ranges=ranges))
    cv2.createTrackbar('MaxR', window_name, 256, 256, partial(onTrackbar, channel='r', min_max='max',window_name=window_name, image=image, ranges=ranges))

    file_name = 'limits.json'
    with open(file_name, 'w') as file_handle:
        print('writing dictionary d to file ' + file_name)
        json.dump(ranges, file_handle) # d is the dicionary

    cv2.waitKey(0)

if __name__ == '__main__':
    main()