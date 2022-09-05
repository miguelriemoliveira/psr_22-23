#!/usr/bin/python3
import argparse
import copy
import time
import colorama
import cv2
import numpy as np

def main():

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1', required=True, type=str, help='Path to image')
    args = vars(parser.parse_args())

    # Load image
    image_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    image_b, image_g, image_r = cv2.split(image_rgb)

    ranges = {'b': {'min': 0, 'max': 100},
              'g': {'min': 80, 'max': 256},
              'r': {'min': 0, 'max': 100}}

    # Processing
    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(image_rgb, mins, maxs)
    # conversion from numpy from uint8 to bool
    mask = mask.astype(np.bool)


    image_processed = (copy.deepcopy(image_rgb))
    image_processed[np.logical_not(mask)] = (image_processed[np.logical_not(mask)] * 0.4).astype(np.uint8)
    image_processed[mask] = (0,255,0)
    # image_processed[mask] = (image_processed[mask] * 0.4).astype(np.uint8)

    print(image_rgb.dtype)
    print(mask.dtype)
    print(image_processed.dtype)

    # Visualization
    cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('original', image_rgb)  # Display the image
    cv2.imshow('mask', mask.astype(np.uint8)*255)  # Display the image
    cv2.imshow('image_processed' , image_processed)  # Display the image


    cv2.waitKey(0)  # wait for a key press before proceeding

if __name__ == '__main__':
    main()
