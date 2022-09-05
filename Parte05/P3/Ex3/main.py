#!/usr/bin/python3
import argparse
import copy
from functools import partial

import cv2
import numpy as np

# Function -----------------------------------
def onTrackbar(value, channel, min_max, wname, ranges, image):
    ranges[channel][min_max] = value  # update corresponding value in ranges dict

    # Processing
    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(image, mins, maxs)
    mask = mask.astype(bool)  # conversion from numpy from uint8 to bool

    image_processed = copy.deepcopy(image)
    image_processed[np.logical_not(mask)] = 0
    cv2.imshow(wname, image_processed)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    # Variables
    wname = 'Segmentation'
    ranges = {'b': {'min': 0, 'max': 256},
              'g': {'min': 0, 'max': 256},
              'r': {'min': 0, 'max': 256}}

    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    cv2.namedWindow(wname)
    cv2.imshow(wname, image)

    cv2.createTrackbar('MinB', wname, 0,   256, partial(onTrackbar, channel='b', min_max='min',wname=wname, image=image, ranges=ranges))
    cv2.createTrackbar('MaxB', wname, 256, 256, partial(onTrackbar, channel='b', min_max='max',wname=wname, image=image, ranges=ranges))
    cv2.createTrackbar('MinG', wname, 0,   256, partial(onTrackbar, channel='g', min_max='min',wname=wname, image=image, ranges=ranges))
    cv2.createTrackbar('MaxG', wname, 256, 256, partial(onTrackbar, channel='g', min_max='max',wname=wname, image=image, ranges=ranges))
    cv2.createTrackbar('MinR', wname, 0,   256, partial(onTrackbar, channel='r', min_max='min',wname=wname, image=image, ranges=ranges))
    cv2.createTrackbar('MaxR', wname, 256, 256, partial(onTrackbar, channel='r', min_max='max',wname=wname, image=image, ranges=ranges))

    # add code to create the trackbar ...
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
